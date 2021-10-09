# Koodoo
Koodoo Technical test

# Part A
Put together a script or program (using any language or technology of your choice) that:

1. Retrieves "Top Stories" from this parliament data RSS feed endpoint: https://www.europarl.europa.eu/rss/doc/top-stories/en.xml
2. Outputs a CSV file of the data.

# Part B
Write a README walkthrough guide which explains how to use your script, any installation steps and any bits of information required to help someone else run the script.
We recommend that you spend more time on this walkthrough / document than the actual script itself and really focus on the developer experience of using, and running your script.

============================================================================================

## Installation

For installation on new system, User can clone the git or just copy paste the python script file along with requirements.txt file to the destination on the server and start using it then and there.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.
All libraries come with python except Pandas(non standard library)

```bash
pip install -f requirements.txt
```

## Usage
=>python fetch_top_stories_eu_parliament.py

Arguments are optional.
There is flexiblity provided for user to provide rss feed point and output csv filename. It can be run as below example

```bash
CMD>python fetch_top_stories_eu_parliament.py  --url=https://www.europarl.europa.eu/rss/doc/top-stories/en.xml --output_csv_filename=eu-rss.csv
```

So in future, if the rss source endpoint is changed or a different rss endpoint is required, script will not require any code change.
