#encoding: utf8

from bs4 import BeautifulSoup
from collections import Counter
from itertools import combinations
import json

with open('data/bookmarks_public_20171214_222058.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

links = soup.find_all('a')

tags = [link.get('tags').split(',') for link in links]

nodes = set()
edges = Counter()
graph = {}

for tags_tuple in tags:
    nodes.update(tags_tuple)
    for combination in combinations(tags_tuple, 2):
        edges[combination] += 1

graph["nodes"] = [{"id": node, "caption": node} for node in nodes]
graph["edges"] = [{"source": t[0], "target": t[1], "type": str(num)}
                  for t, num in edges.most_common()]

with open('static/tags.json', 'w', encoding='utf8') as tags_file:
    json.dump(graph, tags_file, ensure_ascii=False)