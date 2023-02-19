# Triest

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# https://snap.stanford.edu/data/feather-lastfm-social.html
# https://snap.stanford.edu/data/ego-Facebook.html
df = pd.read_csv("facebook_combined_edit.csv")
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
# G = nx.lollipop_graph(4, 6)
edgeList = G.edges()
nodeList = G.nodes()
triangles = list()

nodesSet = set()
edgeSet = set()
trianglesCounter = 0


def append_edge(u, v):
    global trianglesCounter
    global nodesSet
    global edgeSet
    nodesSet.add(u)
    nodesSet.add(v)

    edgeSet.add((u, v))

    for t in nodesSet:
        if ((u, t) in edgeSet or (t, u) in edgeSet) and ((v, t) in edgeSet or (t, v) in edgeSet):
            trianglesCounter += 1
    try:
        return trianglesCounter / (len(edgeSet) * (len(edgeSet) - 1) * (len(edgeSet) - 2))
    except Exception:
        return 0


trianglesEstimate = 0
for u, v in edgeList:
    trianglesEstimate = append_edge(u, v)
    # print(f'Triangles estimate: {trianglesEstimate:.4f}')

print(f'Triangles estimate: {trianglesEstimate:.4f}')
nx.draw(G, with_labels=True)
plt.show()

end_time = datetime.now()
print("Execution time:", end_time - start_time)
