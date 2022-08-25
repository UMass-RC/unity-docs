# Unity Cluster User Documentation
User Documentation for Unity Cluster at UMass Amherst

### Contributing
1. Install mkdocs: `pip install mkdocs`
1. Install the theme: `pip install mkdocs-material`
1. Install a plugin: `pip install mkdocs-include-markdown-plugin`
1. Navigate to the root of the repository and run `mkdocs serve`, which will start a web server you can reach from your local browser to test live edits on documentation.

### Updating the nodelist/partitionlist Tables
edit the tables [here](https://docs.google.com/spreadsheets/d/1kEieN7qKY-iiSJc18SVZdyRnJ4NArIhZY_or_WKnIAI/edit?usp=sharing)

get the [private key](https://drive.google.com/file/d/1Q9fJ0QSi3AjLq3vb4e-1kRQgM1NR7eaA/view?usp=sharing) into `unity-docs/sheets-to-md/unity-sheets-key.json`

Install Python modules
```
pip install gspread
pip install tabulate
pip install oauth2client
pip install pandas
```

Generate the tables
```
cd unity-docs/sheets-to-md
./sheets-to-md.py
```
# comment