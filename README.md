# Docky File Format

This is the compiler for the docky file format.

```console
docker run \
  --rm --user $(id -u):$(id -g) -v "$(pwd -W)":/data \
  micheleforese/latex:full \
  latex \
    --enable-write18 -output-directory=out \
    build/8df13cefe00ecf7f1379482269bf89d22a667aaa.latex
```

```console
docker run \
  --rm --user $(id -u):$(id -g) -v "$(pwd -W)":/data \
  micheleforese/latex:full \
  dvisvgm \
  --output="%f.svg" \
  24d7d4162982051b8cb17d339f5d6e1272cbb6d1.dvi
```

```console
docker run \
  --rm -it --user $(id -u):$(id -g) -v "$(pwd -W)":/data \
  micheleforese/latex:full \
  dvisvgm --list-specials
```

```console
docker run \
  --rm -it -v "$(pwd -W)":/data \
  micheleforese/latex:full
```

```console
latex --enable-write18 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.tex

pdflatex 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.tex
dvisvgm --pdf --output="%f.svg" 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.pdf



dvisvgm --list-specials
dvisvgm --output="%f.svg" 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.dvi
dvisvgm --bbox=preview --output="%f.svg" 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.dvi


dvisvgm --pdf --output="%f.svg" 24d7d4162982051b8cb17d339f5d6e1272cbb6d1.pdf
```

## Manim

```console
docker run --rm -it --user="$(id -u):$(id -g)" -v "$(pwd -W)\build\manim":/manim manimcommunity/manim \
manim --output_file "cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.mp4" --quality h --renderer opengl cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.py
manim --output_file cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891 --quality h cbf2fba0bd7c8ded79e0bcf0a987e029bc4a4891.py
```

## Ghost Script

Ricordarsi di installare la libreria GhostScript per interpretare
nel modo corretto i component PostScript

```console
apt update && apt install -y ghostscript
```

## Compile LaTeX

Link utili:

- [How To Use LaTeX](https://guides.lib.wayne.edu/latex/compile)
- [dvisvg](https://dvisvgm.de/)
