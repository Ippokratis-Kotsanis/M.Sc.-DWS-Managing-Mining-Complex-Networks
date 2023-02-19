# Compact forward

import matplotlib.pyplot as plt
from datetime import datetime
import networkx as nx
import pandas as pd

start_time = datetime.now()

# https://snap.stanford.edu/data/feather-lastfm-social.html
# https://snap.stanford.edu/data/ego-Facebook.html
df = pd.read_csv("facebook_combined_edit.csv")
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
# G = nx.lollipop_graph(4, 6)
edgeList = G.edges()
nodeList = G.nodes()
triangles = list()
degrees = sorted(G.degree, key=lambda x: x[1], reverse=True)
sortedNodesByDegree = [i[0] for i in degrees]
h = {}
for i in range(0, len(degrees)):
    h[degrees[i][0]] = i
visitedNodes = set()
triangles = list()

for v in sortedNodesByDegree:
    visitedNodes.add(v)
    neighbors = [n for n in G.neighbors(v)]

    for u in [n for n in neighbors if n not in visitedNodes]:
        uNeighbors = G.neighbors(u)
        vNeighbors = G.neighbors(v)

        u_ = next(uNeighbors, None)
        v_ = next(vNeighbors, None)
        while u_ is not None and v_ is not None:
            if h[u_] < h[v_]:
                u_ = next(uNeighbors, None)
            elif h[u_] > h[v_]:
                v_ = next(vNeighbors, None)
            else:
                triangles.append(sorted([u, v, u_]))
                u_ = next(uNeighbors, None)
                v_ = next(vNeighbors, None)
triangles_set = list(set(map(tuple, triangles)))
print(triangles_set)
# nx.draw(G, with_labels=True)
# plt.show()
number_of_triangles = len(triangles_set)
print("Number of triangles:", number_of_triangles)

end_time = datetime.now()
print("Execution time:", end_time - start_time)
