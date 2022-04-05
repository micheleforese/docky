from gettext import install
from typing import List
from rich import inspect

from rich.panel import Panel
from setuptools import find_packages, setup

from docky.console import console

with open("README.md") as f:
    readme: str = f.read()

with open("requirements.txt", "r") as f:
    install_requires: List[str] = f.read().splitlines()
    inspect(install_requires)

setup(
    name="docky",
    version="0.1.0",
    description="Docky compiler",
    long_description=readme,
    author="Michele Forese",
    author_email="michele.forese.personal@gmail.com",
    url="https://github.com/micheleforesedev/docky",
    # license=license,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "docky = docky.script.cli:cli",
        ],
    },
)
