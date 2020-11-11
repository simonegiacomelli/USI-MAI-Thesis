# this script runs on pi
# os dependencies: sudo apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
import os
from pathlib import Path
import time
import subprocess

dir = (Path(__file__) / '../..').resolve().absolute()
print('chdir',dir)
os.chdir(dir)


def run(cmd):
    # print('running [%s]' % (cmd))
    res = os.system(cmd)
    print('exit code %d for [%s]' % (res, cmd))
    return res


def watch():
    run('git fetch --all -q && git pull -q')
    pdf_id = subprocess.getoutput('git log --format="%H" -n 1 auto/main.pdf')
    other_id = subprocess.getoutput('git log --format="%H" -n 1')
    if pdf_id != other_id:
        # need render pdf
        print('Need render pdf. Pdf commit id=%s other commit id=%s' % (pdf_id, other_id))
        res = os.system('pdflatex -interaction nonstopmode --output-directory=auto --aux-directory=auto main.tex')
        if res != 0:
            # compile error
            pass
        os.system("git commit -a -m 'pdflatex auto run' && git push")



while True:
    watch()
    time.sleep(1)
