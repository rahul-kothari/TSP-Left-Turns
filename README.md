# TSP - just allowing Left Turns

Project Scope (rough guidance)
https://docs.google.com/document/d/19NkntFg3GFvIwB5UZ0RwT5NCb02tXNOGPbTSoCklO38/edit?usp=sharing

## Code files
`dijkstra_shortest_path.py` -> carries out dijkstra algorithm b\w 2 nodes given osm graph G

`reduce_graph_for_tsp.py` -> given a list of nodes, does dijkstra for each pair and returns adjacent matrix.

## Setup
### Prerequisites
* Python - 3.6 or greater
* pip 

## Installation
* Open terminal and cd to the directory you want to use for the project

* Git clone the repo:
```
git clone https://github.com/rahul-kothari/TSP-Left-Turns.git
```
You might get access denied errors - in that case try: `git clone https://<YourGitHubUsername>:<YourGithubPassword>@github.com/rahul-kothari/TSP-Left-Turns.git`

* Create python virtual environment
```
python -m venv venv
```

* Activate virtual environment (Windows):
```
venv\Scripts\activate
```

* Install requirements
Unfortunately, our main requirement - osmnx can't be easily installed on windows.
A simple `pip install -r requirements.txt` won't work here.
So follow this script:

```
pip install wheel
pip install pipwin
pip install numpy
pip install python-tsp

pipwin install shapely
pipwin install gdal
pipwin install fiona
pipwin install pyproj
pipwin install six
pipwin install rtree
pipwin install geopandas
pip install osmnx
```
https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda

## Run the project:
```
venv\Scripts\activate
python test.py
```

**OR for quick testing**

```
venv\Scripts\activate
python
```
And use the python shell.

