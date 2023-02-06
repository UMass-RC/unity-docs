from docker.io/python
run pip install mkdocs
run pip install mkdocs-material
run pip install mkdocs-include-markdown-plugin
expose 8080
workdir /unity-docs
cmd ["mkdocs", "serve"]
