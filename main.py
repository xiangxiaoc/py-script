"""
Project main entrypoint
"""
import pathlib
import sys

import typer

'''for typer-cli'''
parent_path = pathlib.Path(__file__).parent
sys.path.append(str(parent_path.absolute()))
import core.cli

app = typer.Typer()
app.add_typer(core.cli.app, name='core')

if __name__ == '__main__':
    app()
