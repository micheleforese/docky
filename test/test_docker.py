import unittest
from docky.console import console
from docky.docker import Docker


class test_docker(unittest.TestCase):
    def test_basic(self):
        """
        Test that it can sum a list of integers
        """

        docker = Docker()
        command = docker.run(
            "micheleforese/latex:2021-full",
            user=(23, 45),
            volume=("D://ciao/stronzo", "/data"),
            command="pdflatex -output-directory={} {}".format(
                "/build", "/build/test.tex"
            ),
        )

        console.print(1 / 0)

        real_command = "docker run --rm --user 23:45 -v D://ciao/stronzo:/data pdflatex -output-directory=/build /build/test.tex"

        self.assertEqual(real_command, command)
