# Unity Cluster User Documentation
User Documentation for Unity Cluster at UMass Amherst

### Contributing
1. Install mkdocs: `pip install mkdocs`
1. Install the theme: `pip install mkdocs-material`
1. Navigate to the root of the repository and run `mkdocs serve`, which will start a web server you can reach from your local browser to test live edits on documentation.

### Updating the nodelist/partitionlist Tables
edit the tables [here](https://docs.google.com/spreadsheets/d/1kEieN7qKY-iiSJc18SVZdyRnJ4NArIhZY_or_WKnIAI/edit?usp=sharing)

get the [private key](https://drive.google.com/file/d/1Q9fJ0QSi3AjLq3vb4e-1kRQgM1NR7eaA/view?usp=sharing) into the same directory as sheets-to-md.py

Install Python modules
```
pip install gspread
pip install tabulate
pip install oauth2client
pip install pandas
```

```
cd unity-docs/sheets-to-md
./sheets-to-md.py
```
this generates a markdown document for each table.

copy paste the markdown into the following files:

`*-nodes.md` go into technical/nodelist

`*-parts.md` go into technical/partitionlist
