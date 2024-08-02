from pathlib import Path
from typing import Optional

from pagehub.constants import SUPPORT_FORMATS
from pagehub.enums import ExportFormat
from pagehub.settings import pagehub_settings
from pagehub.utils.datetime_utils import get_now_str
from pagehub.utils.export_utils import export

STORAGE = pagehub_settings.STORAGE


def export_task(url: str, format: Optional[list[str]] = None):
    format = None or SUPPORT_FORMATS
    directory = Path(STORAGE["path"]).absolute() / get_now_str()
    path_lst, info = export(url, directory, [ExportFormat(i) for i in format])
    return path_lst, info


def notion_push_task(
    url: str,
    api_token: str,
    token_v2: Optional[str] = None,
    title: str = "",
    format: Optional[list[str]] = None,
):
    path_lst, info = export_task(url, format)
    title = title or info["title"]
    # TODO


if __name__ == "__main__":
    export_task("https://www.baidu.com", ["PDF"])
