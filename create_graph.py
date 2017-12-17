#encoding: utf8

from collections import Counter
from itertools import combinations
import json
import sys

from bs4 import BeautifulSoup

data_file = sys.argv[0]

# Extraction of the tags
with open(data_file) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

links = soup.find_all('a')
tags = [link.get('tags').split(',') for link in links]

# Creation of the structure
nodes = set()
edges = Counter()
graph = {}

# Extraction of edges and nodes
for tags_tuple in tags:
    nodes.update(tags_tuple)
    for combination in combinations(tags_tuple, 2):
        edges[combination] += 1

graph["nodes"] = [{"id": node, "caption": node} for node in nodes]
graph["edges"] = [{"source": t[0], "target": t[1], "type": str(num)}
                  for t, num in edges.most_common()]

# Write in the final graph file
with open('static/tags.json', 'w', encoding='utf8') as tags_file:
    json.dump(graph, tags_file, ensure_ascii=False)
