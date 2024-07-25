import click
from click import ParamType


class MultipleChoice(click.Choice):
    def convert(self, value, param, ctx):
        values = [v.strip() for v in value.split(",")]
        normed_values = list()
        for v in values:
            normed_values.append(super().convert(v, param, ctx))
        return normed_values

    def get_metavar(self, param: ParamType) -> str:
        choices_str = ",".join(self.choices)
        return f"[{choices_str}]"
