from pathlib import Path
from typing import Optional

from pagehub.constants import SUPPORT_FORMATS
from pagehub.enums import ExportFormat
from pagehub.record.models import Snapshot, SnapshotResult
from pagehub.settings import pagehub_settings
from pagehub.utils.datetime_utils import get_now_str
from pagehub.utils.export_utils import export

STORAGE = pagehub_settings.STORAGE


def export_task(snapshot_id: int, url: str, format: Optional[list[str]] = None):
    snapshot = Snapshot.objects.get(pk=snapshot_id)

    format = None or SUPPORT_FORMATS
    base_directory = Path(STORAGE["path"]).absolute()
    directory = base_directory / str(snapshot.uuid) / get_now_str()

    path_lst, info = export(url, directory, [ExportFormat(i) for i in format])
    for info in path_lst:
        path = str(Path(info["path"]).relative_to(base_directory))
        SnapshotResult.objects.create(
            snapshot=snapshot, format=info["format"], path=path
        )
    snapshot.title = info.get("title", "")
    snapshot.save(update_fields=["title"])

    return path_lst, info


def notion_push_task(
    snapshot_id: int,
    url: str,
    api_token: str,
    token_v2: Optional[str] = None,
    title: str = "",
    format: Optional[list[str]] = None,
):
    path_lst, info = export_task(snapshot_id, url, format)
    title = title or info["title"]
    # TODO


if __name__ == "__main__":
    export_task("https://www.baidu.com", ["PDF"])
