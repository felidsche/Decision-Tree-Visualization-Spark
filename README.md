# Decision Tree Visualization for Apache Spark
## Why?
Apache Spark provides its users the ability to implement Decision Trees algorithms in a very efficient way, however the output seems to be not so friendly for non-technical users. So this project is an attempt to visualize Collapsible Decision Trees using [D3.js](https://d3js.org/), by parsing the nested conditional statements to a [JSON](http://www.json.org/) format, and using it as dataset for display.

## Languages & Technologies Used
- (Apache Spark)
- Python 3.9
- HTML
- JavaScript
- D3.js

## Usage
1. copy the `str` value of your Decision Tree `model.toDebugString` in `DT.py`
2. run `DT.py` to create `data/structure.json`
- run `visualize.html` on `localhost` (e.g. let PyCharm be your Webserver) to see the horizontal tree

## Example
