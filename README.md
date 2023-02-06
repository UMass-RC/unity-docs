# Unity Cluster User Documentation
User Documentation for Unity Cluster at UMass Amherst

### Contributing

#### Github Guidelines
We will use branches to propose changes.

Guide for basic git commands: [https://github.com/git-guides](https://github.com/git-guides)

1. Clone the repository using Github Desktop or ssh/https/git-cli.
1. Make a new branch from `main` while following the namescheme: `<author>/<change-description>`
1. Setup the local environment to run the documentation locally (described below).
1. Make the desired changes.
1. [Commit](https://github.com/git-guides/git-commit) and [Push](https://github.com/git-guides/git-push) the changes to your branch.
1. Create a [Pull Request](https://docs.github.com/en/pull-requests) while comparing your branch to `main`.
1. List `tlbernardin` and another team member for review. 
1. Write a good description for the changes proposed no matter how small. 
1. Submit [Pull Request](https://docs.github.com/en/pull-requests).

#### Local Setup
1. Install mkdocs: `pip install mkdocs`
1. Install the theme: `pip install mkdocs-material`
1. Install a plugin: `pip install mkdocs-include-markdown-plugin`
1. Navigate to the root of the repository and run `mkdocs serve`, which will start a web server you can reach from your local browser to test live edits on documentation.

#### Container Setup
You can also build the documentation using a containerized environment.
The following steps can be accomplished via either
[Docker](https://www.docker.com/) or [podman](https://podman.io/).

```
podman build -v $(pwd):/unity-docs:z -t unity-docs .
podman run -v $(pwd):/unity-docs:z -p 8080:8080 unity-docs
```

Once the above has completed, you can view the live documentation at
http://localhost:8080.

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

Upload the new tables back to git
