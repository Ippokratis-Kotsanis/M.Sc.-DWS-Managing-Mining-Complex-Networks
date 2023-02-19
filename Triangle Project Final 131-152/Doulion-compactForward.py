# Doulion & compactForward

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
# Approximate algorithm. Remove some edges to simplify the initial graph. Sparcification
# For every edge throw a coin that has propability p to happen and 1-p not to happen. If p
# exists keep edge, else delete it.
# As far as I reduce p, the graph becomes more sparce (arraionei)

from numpy.random import choice
import networkx as nx

start_time = datetime.now()

# https://snap.stanford.edu/data/feather-lastfm-social.html
# https://snap.stanford.edu/data/ego-Facebook.html
df = pd.read_csv("facebook_combined_edit.csv")
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
# G = nx.lollipop_graph(4, 6)
edge_labels = nx.get_edge_attributes(G, "weight")
p = 0.8
for edge in G.edges():
    Coin_Results = ["Success", "Failure"]
    Coin_Result = choice(Coin_Results, p=[p, 1-p])
    # print(Coin_Result)
    if Coin_Result == "Success":
        G[edge[0]][edge[1]]["weight"] = 1/p
        # print(G[edge[0]][edge[1]]["weight"])
    else:
        G.remove_edge(*edge)
# print(nx.get_edge_attributes(G, 'weight'))

# Add compact forward algorithm
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
# nx.draw(G, with_labels=True)
# plt.show()
print("Triangles are:", triangles_set)
number_of_triangles = len(triangles_set)
print("Number of triangles:", number_of_triangles)
My_real_number_of_trinagles = number_of_triangles * ((1/p)**3)
print("Final number of triangles", My_real_number_of_trinagles)

end_time = datetime.now()
print("Execution time:", end_time - start_time)



