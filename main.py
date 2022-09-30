import sys

import typer
import os

import util.log

# 在任意目录执行脚本时，python 进程都会临时切换到脚本所在目录再执行
dir_path, script_name = os.path.split(__file__)
if dir_path != '':
    os.chdir(dir_path)

print(sys.path)

app = typer.Typer()


@app.command()
def version():
    print('version')


@app.command()
def hello(name: str):
    print(f'hello {name}')


if __name__ == '__main__':
    print(sys.path)

    logger = util.log.get_logger()
    logger.info('123')

    app()
