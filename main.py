"""
Project main entrypoint
"""
import logging.config
import os
import pathlib
import sys
from typing import Optional

import typer

""" 
Adding project root path into sys.path
for typer-cli(typer command) to discover python module in project
"""
parent_path = pathlib.Path(__file__).parent
sys.path.append(str(parent_path.absolute()))

import settings

""" For supporting relative path configured in settings.py. change dir to project root path """
dir_path, script_name = os.path.split(__file__)
if dir_path != '':
    os.chdir(dir_path)
os.makedirs(settings.LOGDIR_BASE_PATH, exist_ok=True)
logging.config.dictConfig(settings.LOGGING_CONFIG)  # will create log file defined in LOGGING_CONFIG when run this line

# """ if this project has only one app, import app(typer.Typer) directly """
# from cli.app1.main_cli import app
#
# """single app cli end"""

""" 
If your project has multiple apps, 
import packages then use app.add_typer to add their own app object to avoid variable name conflict 
"""
from cli import app1_cli
from cli import app2_cli

app = typer.Typer()
app.add_typer(app1_cli.app, name=app1_cli.__app_name__)
app.add_typer(app2_cli.app, name=app2_cli.__app_name__)

__app_name__ = 'main'
__version__ = '0.0.1'


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
    """ main description """
    return


""" multiple apps end """

if __name__ == '__main__':
    app()
