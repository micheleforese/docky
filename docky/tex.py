from collections import UserDict
from msilib.schema import Error
from optparse import Option
from os import error, remove
import os
from typing import List, Optional
from venv import create
import xml.etree.ElementTree as ET
from xml.sax.saxutils import XMLFilterBase
from rich.console import Console
import hashlib
import subprocess
import docker

console = Console()


def create_latex_file(latex: str):
    latex_item_hash = hashlib.sha1(latex.encode())
    console.log(latex_item_hash.hexdigest())

    if(
        os.path.isfile('./build/{}.tex'.format(latex_item_hash.hexdigest())) and
        os.path.isfile('./build/{}.dvi'.format(latex_item_hash.hexdigest())) and
        os.path.isfile('./build/{}.svg'.format(latex_item_hash.hexdigest()))
    ):
        console.log("File already exists.")
        return

    latex_packages = r"\usepackage{tikz,tikz-3dplot}" + "\n" + \
        r"\usepackage{amsmath}" + "\n" + \
        r"\usepackage{mathtools}" + "\n" + \
        r"\usepackage[thinc]{esdiff}" + "\n" + \
        r"\usepackage[utf8]{inputenc}" + "\n" + \
        r"\usepackage[italian]{babel}" + "\n" + \
        r"\usepackage{textcomp,gensymb}" + "\n" + \
        r"\usepackage{bm}" + "\n" + \
        r"\usepackage{calc}" + "\n" + \
        r"\usepackage{physics}" + "\n" + \
        r"\usepackage{adjustbox}" + "\n" + \
        r"\usepackage{balance}" + "\n" + \
        r"\usepackage{pgfplots}" + "\n" + \
        r"\usepackage{subfiles}" + "\n" + \
        r"\usepackage{graphicx}" + "\n" + \
        r"\usepackage{url}" + "\n" + \
        r"\usepackage{siunitx}" + "\n" + \
        r"\DeclareSIUnit\px{px}" + "\n" + \
        r"\usepackage{pst-optic, pst-optexp}" + "\n" + \
        r"\pgfplotsset{compat=1.18}" + "\n"

    latex_udc = r"\newcommand{\der}[3][]{\frac{d^{#1} #2}{d #3^{#1}}}" + "\n" + \
        r"\newcommand{\dder}[3][]{\frac{\partial{d}^{#1} #2}{\partial{d} #3^{#1} }}" + "\n" + \
        r"\newcommand{\uvec}[1]{\hat{#1}}" + "\n" + \
        r"\newcommand{\cvec}[2]{#1\uvec{#2}}" + "\n" + \
        r"\newcommand{\veccomp}[4][]{\cvec{#2}{i^{#1}} + \cvec{#3}{j^{#1}} + \cvec{#4}{k^{#1}}}" + "\n"

    latex_udc = ""

    latex_start = \
        r"\documentclass[preview]{standalone}" + "\n" + \
        latex_packages + \
        latex_udc + \
        r"\begin{document}" + "\n"

    latex_end = "\n" + r"\end{document}"

    latex_complete = "{0}{2}{1}".format(
        latex_start, latex_end, latex)

    latex_file_path = "build/{}.tex".format(latex_item_hash.hexdigest())
    console.log("Latex file path: " + latex_file_path)

    with open(latex_file_path, "w") as f:
        f.write(latex_complete)

    out_directory = "build"

    # console.log(client.containers.run('alpine', 'echo hello world'))

    docker_image = "micheleforese/latex:full"

    # Get PWD
    # pwd, stderr = exec_command(['pwd'])
    pwd = os.getcwd()
    console.log("PWD: " + pwd)

    # Get User ID and GROUP
    user_id, stderr = exec_command(['id', '-u'])
    console.log(user_id)
    console.log(stderr)
    user_group, stderr = exec_command(['id', '-g'])
    console.log(user_group)
    console.log(stderr)

    command = [
        r'docker', r'run',
        r'--rm',
        r'--user', r'{}:{}'.format(''.join(filter(str.isdigit, user_id)),
                                   ''.join(filter(str.isdigit, user_group))
                                   ),
        r'-v', r'{}:/data'.format(pwd),
        docker_image,
        'pdflatex',
        '-output-directory={}'.format(out_directory),
        '{}'.format(latex_file_path),
    ]

    console.print(command)

    stdout, stderr = exec_command(command)

    console.log("RESULT:" + stdout)
    console.log("ERROR" + stderr)

    command = [
        r'docker', r'run',
        r'--rm',
        r'--user', r'{}:{}'.format(''.join(filter(str.isdigit, user_id)),
                                   ''.join(filter(str.isdigit, user_group))
                                   ),
        r'-v', r'{}\{}:/data'.format(pwd, out_directory),
        docker_image,
        'dvisvgm',
        '--pdf',
        '--output="build/{}.svg"'.format(latex_item_hash.hexdigest()),
        '{}.pdf'.format(latex_item_hash.hexdigest()),
    ]
    console.print(command)

    stdout, stderr = exec_command(command)

    console.log(stdout)
    console.log(stderr)
