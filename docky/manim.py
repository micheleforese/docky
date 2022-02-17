import hashlib
import os

from docky.console import console
from docky.docky import Docky, exec_command
from docky.plugin import Plugin
from docky.utility import hash


class Manim(Plugin):
    build_path: os.path = 'build/manim'
    pass


def create_manim_file(manim: str):
    manim = r"from manim import *" + "\n" + manim

    manim_hash = hash(manim)
    console.log(manim_hash.hexdigest())

    if(
        os.path.isfile('./build/manim/{}.manim'.format(manim_hash.hexdigest())) and
        os.path.isfile('./build/manim/{}.mp4'.format(manim_hash.hexdigest()))
    ):
        console.log("File already exists.")
        return

    manim_file_path = "build/manim/{}.manim".format(manim_hash.hexdigest())
    console.log("Manim file path: " + manim_file_path)

    with open(manim_file_path, "w") as f:
        f.write(manim)

    out_directory = r"build\manim"

    # console.log(client.containers.run('alpine', 'echo hello world'))

    docker_image = "manimcommunity/manim"

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
        r'-v', r'{}\build\manim:/manim'.format(pwd),
        docker_image,
        'manim',
        '-pql',
        '--output_file={}'.format(manim_file_path),
        '{}'.format(manim_file_path),
    ]

    console.print(command)

    stdout, stderr = exec_command(command)

    console.log("RESULT:" + stdout)
    console.log("ERROR" + stderr)
