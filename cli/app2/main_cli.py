import logging
import pathlib
import sys
from typing import Optional

import typer

parent_path = pathlib.Path(__file__).parent.parent
sys.path.append(str(parent_path.absolute()))
from cli.app2 import __version__, __app_name__

logger = logging.getLogger(__app_name__)

app = typer.Typer()


# """Add subTyper"""
# app.add_typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True,
        )
) -> None:
    """ app2 description """
    return


if __name__ == '__main__':
    app()
