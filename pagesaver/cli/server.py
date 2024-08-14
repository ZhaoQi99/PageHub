import asyncio

import click
from hypercorn.asyncio import serve
from hypercorn.config import Config

from pagehub.core.asgi import application
from pagehub.settings import pagehub_settings


@click.command("server")
@click.help_option("-h", "--help")
@click.option(
    "-b",
    "--bind",
    "bind",
    show_default=True,
    default=pagehub_settings.SERVER_BIND,
    help="The TCP host/address to bind to.",
)
def server_command(*args, **kwargs):
    """Run PageHub HTTP server"""
    config = Config.from_mapping({"bind": pagehub_settings.SERVER_BIND}, **kwargs)
    asyncio.run(serve(application, config))
