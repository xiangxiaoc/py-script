from . import main_cli, __app_name__


def main():
    main_cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
