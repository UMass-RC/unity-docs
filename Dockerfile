from docker.io/python
copy entrypoint.sh /entrypoint.sh
run chmod +x /entrypoint.sh
entrypoint ["/entrypoint.sh"]
run pip install mkdocs
run pip install mkdocs-material
run pip install mkdocs-include-markdown-plugin
# install spreadsheet to markdown dependencies
run pip install gspread
run pip install tabulate
run pip install oauth2client
run pip install pandas
expose 8080
workdir /unity-docs
cmd ["mkdocs", "serve", "--dev-addr=0.0.0.0:8080"]
