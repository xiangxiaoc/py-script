import typer

import util.log

app = typer.Typer()

@app.command()
def version():
    print('version')

@app.command()
def hello(name: str):
    print(f'hello {name}')


if __name__ == '__main__':

    logger = util.log.get_logger()
    logger.info('123')



    app()