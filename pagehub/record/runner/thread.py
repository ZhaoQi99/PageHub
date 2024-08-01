from .base import BaseRunner


class BackgroundThreadRunner(BaseRunner):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass
