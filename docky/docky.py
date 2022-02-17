import hashlib
import os
import subprocess
import xml.etree.ElementTree as ET
from collections import UserDict
from html.entities import html5
from html.parser import HTMLParser
from msilib.schema import Error
from optparse import Option
from os import error, remove
from typing import List, Optional
from venv import create
from xml.sax.saxutils import XMLFilterBase

import docker

from docky.console import console


class Docky(HTMLParser):
    parser = HTMLParser()

    def __init__(self) -> None:
        console.log("init")
        self.parser.feed(
            '''
            <html>
              <head>
                <title>Test</title>
              </head>
              <body>
              </body>
            </html>
            '''
        )
        console.print(self.parser)


class xml:
    tree: Optional[ET.ElementTree]

    def __init__(self, file_path: os.path) -> None:
        self.tree = ET.parse(file_path)

    def open(self, file_path: os.path):
        self.tree = ET.parse(file_path)

    def get_tree(self):
        return self.tree

    def get_root(self):
        if(self.tree != None):
            return self.tree.getroot()


def exec_command(command):
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()
    try:
        stdout = stdout.decode('utf-8')
        stderr = stderr.decode('utf-8')
    except:
        pass
    return stdout, stderr
