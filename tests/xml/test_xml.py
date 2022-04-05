from pathlib import Path
import pytest


from docky import utility
from docky.console import console
from docky.docky import Docky


def test_xml_parsing():

    docky = Docky()

    docky.compile(Path.cwd() / "test/xml/test_xml.docky")

    assert 1 == 1
