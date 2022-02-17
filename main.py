from docky.console import console
from xml.dom import minidom
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
from docky.tex import *
from docky.manim import *
from docky.docky import *

console = Console()
client = docker.from_env()


def test_tex():

    xml_file = xml("test/tex/tex.docky")
    root = xml_file.get_root()

    tree = xml_file.get_tree()

    for item in tree.iter():
        console.print(
            "[blue]<{0}>[/]\n\t{1}\n[blue]</{0}>[/]".format(item.tag, item.text.strip()))
        pass

    latex_items = root.findall('latex')

    for item in latex_items:
        latex_text = item.text.strip()
        console.log(latex_text)

        create_latex_file(latex_text)


def test_manim():
    xml_file = xml("test/manim/manim.docky")
    root = xml_file.get_root()
    tree = xml_file.get_tree()

    manim_items = root.findall('manim')

    # docker run --rm -it  --user="$(id -u):$(id -g)" -v "$(pwd -W)":/manim manimcommunity/manim

    for item in manim_items:
        item_text = item.text.strip()
        console.log(item_text)

        create_manim_file(item_text)


# test_manim()
# docky = Docky()

document = """
<?xml version="1.0"?>
<company>
    <name>GeeksForGeeks Company</name>
    <staff id="1">
        <name>Amar Pandey</name>
        <salary>8.5 LPA</salary>
    </staff>
    <staff id="2">
        <name>Akbhar Khan</name>
        <salary>6.5 LPA</salary>
    </staff>
    <staff id="3">
        <name>Anthony Walter</name>
        <salary>3.2 LPA</salary>
    </staff>
</company>
"""

doc = minidom.parseString(document)
name = doc.getElementsByTagName("name")[0]
console.print(name.firstChild.data)
