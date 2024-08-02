from functools import cached_property

from django.db import models

from pagehub.enums import ExportFormat
from pagehub.lib.base.models import BaseModelWithUUID


class Snapshot(BaseModelWithUUID):
    url = models.URLField(db_index=True)
    title = models.CharField(max_length=512, default="", blank=True, db_index=True)

    @cached_property
    def size(self):
        pass

    class Meta:
        verbose_name = "快照"
        verbose_name_plural = verbose_name
        db_table = "snapshot"


class SnapshotResult(BaseModelWithUUID):
    FORMAT_CHOICES = (
        (ExportFormat.PDF.value, "PDF"),
        (ExportFormat.MHTML.value, "MHTML文件"),
    )
    snapshot = models.ForeignKey(Snapshot, on_delete=models.CASCADE)
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    path = models.FileField()

    class Meta:
        unique_together = ("snapshot", "format")
        verbose_name = "快照结果"
        verbose_name_plural = verbose_name
        db_table = "snapshot_result"
