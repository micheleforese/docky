# LaTeX

## Compile to HTML

```console
docker run --rm -it --user $(id -u):$(id -g) -v "$(pwd -W)":/data micheleforese/latex:2021-full htlatex <file_name>
```
