"""core entry point script. for using 'python -m core'"""
# cip/__main__.py

from core import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
