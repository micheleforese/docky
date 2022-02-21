from setuptools import setup, find_packages
import os


with open("README.md") as f:
    readme = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

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
)
