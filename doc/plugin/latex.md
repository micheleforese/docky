# LaTeX

## Compile LaTeX

Link utili:

- [How To Use LaTeX](https://guides.lib.wayne.edu/latex/compile)
- [dvisvg](https://dvisvgm.de/)

## Compile to HTML

```console
docker run --rm -it --user $(id -u):$(id -g) -v "$(pwd -W)":/data micheleforese/latex:2021-full htlatex <file_name>
```

## dvisvgm Library

```console
docker run \
  --rm -it --user $(id -u):$(id -g) -v "$(pwd -W)":/data \
  micheleforese/latex:full \
  dvisvgm --list-specials
```

## Ghost Script

Ricordarsi di installare la libreria GhostScript per interpretare
nel modo corretto i component PostScript

```console
apt update && apt install -y ghostscript
```
