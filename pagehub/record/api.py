from typing import Optional

from ninja import Field, Query, Router, Schema

from pagehub.enums import ExportFormat
from pagehub.record.runner import BackgroundThreadRunner
from pagehub.record.tasks import export_task, notion_push_task

router = Router()


class RecordFilters(Schema):
    format: list[ExportFormat] = Field(
        default=list(ExportFormat.__members__.values()),
    )


@router.get("/{path:url}")
def record(request, url: str, filters: Query[RecordFilters]):
    runner = BackgroundThreadRunner()
    runner.add_task(export_task, url, **filters.model_dump(mode="json"))
    runner.start()
    return {
        "url": url,
        "params": filters.model_dump(mode="json"),
    }


class NotionFilters(RecordFilters):
    api_token: str
    token_v2: Optional[str] = None
    title: Optional[str] = "-"


@router.get("/notion/{path:url}")
def notion_record(request, url: str, filters: Query[NotionFilters]):
    runner = BackgroundThreadRunner()
    runner.add_task(export_task, url, {})
    runner.add_task(notion_push_task, url, **filters.model_dump(mode="json"))
    runner.start()
    return {"url": url}
