import click

from pagehub import __version__

VERSION = rf"""
        ____                  _       _   _       _
        |  _ \ __ _  __ _  ___| |__   | | | |_   _| |__
        | |_) / _` |/ _` |/ _ \ '_ \  | |_| | | | | '_ \
        |  __/ (_| | (_| |  __/ | | | |  _  | |_| | |_) |
        |_|   \__,_|\__, |\___|_| |_| |_| |_|\__,_|_.__/
                    |___/

                    VERSION {__version__}
"""


@click.group()
@click.version_option(__version__, "-v", "--version", message=VERSION)
@click.help_option("-h", "--help")
def main():
    pass


from .export import export

main.add_command(export)
