# Manim Plugin

## Manim Basics

```console
docker run --rm -it --user="$(id -u):$(id -g)" -v "$(pwd -W)\build\manim":/manim manimcommunity/manim \
manim --output_file "cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.mp4" --quality h --renderer opengl cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.py
manim --output_file cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891 --quality h cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.py
```
