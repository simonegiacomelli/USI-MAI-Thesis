import os
from pathlib import Path
import time

dir = (Path(__file__) / '../..').resolve().absolute()
os.chdir(dir)


def run(cmd):
    # print('running [%s]' % (cmd))
    res = os.system(cmd)
    print('exit code %d for [%s]' % (res, cmd))
    return res


while True:
    if run('git pull -q') != 0:
        # changes incoming
        print('ok')
    time.sleep(5)

res = os.system('pdflatex -interaction nonstopmode --output-directory=auto --aux-directory=auto main.tex')
if res == 0:
    os.system("git commit -a -m 'pdflatex auto run'")
