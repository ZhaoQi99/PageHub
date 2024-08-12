from datetime import timedelta

import click
from django.core.management import call_command
from django.utils import timezone

from pagehub import __version__


@click.command("init")
@click.help_option("-h", "--help")
def init_command(*args, **kwargs):
    """Initialize PageHub"""
    click.secho(f"[+] Initializing PageHub v{__version__}...", fg="green")
    click.secho("{}\n".format("-" * 30), fg="green")

    click.secho("[+] Creating database and running initial migrations...", fg="green")
    call_command("migrate")

    click.secho("\n{}".format("-" * 30), fg="green")
    click.secho("[√] Init successfully.", fg="green")

    from pagehub.authorization.models import APIToken

    expired = timezone.now().astimezone() + timedelta(days=365 * 100)
    token = APIToken.objects.create(expired=expired)
    click.echo(
        "Your API token: {token} (expired: {expired})".format(
            token=click.style(token.token, fg="blue"),
            expired=click.style(expired.strftime("%Y-%m-%d %H:%M:%S"), fg="red"),
        )
    )

    click.echo(
        """
{hint} To start PageHub, run: 
    pagehub server # then visit http://127.0.0.1:8000
        """.format(
            hint=click.style("Hint:", fg="magenta")
        )
    )
