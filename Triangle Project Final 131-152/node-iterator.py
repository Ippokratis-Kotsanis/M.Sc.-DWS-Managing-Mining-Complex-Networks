# Node iterator

from datetime import datetime
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

start_time = datetime.now()

# https://snap.stanford.edu/data/feather-lastfm-social.html
# https://snap.stanford.edu/data/ego-Facebook.html
df = pd.read_csv("facebook_combined_edit.csv")
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
edgeList = G.edges()
nodeList = G.nodes()
triangles = list()
for i in range(0, len(nodeList) - 1):
    neigbors = list(G.neighbors(i))
    pairs_Of_Nodes_in_Neighbors = [(a, b) for idx, a in enumerate(neigbors) for b in neigbors[idx + 1:]]
    for pair in pairs_Of_Nodes_in_Neighbors:
        for edge_pair in edgeList:
            if pair == edge_pair:
                triangle_pair_of_i = list(pair)
                triangle_pair_of_i.append(i)
                triangles.append(sorted(tuple(triangle_pair_of_i)))
                triangle_pair_of_i.clear()
triangles_set = list(set(map(tuple, triangles)))  # remove duplicate triangles
print("Triangles are:", triangles_set)
# nx.draw(G, with_labels=True)
# plt.show()
number_of_triangles = len(triangles_set)
print("Number of triangles:", number_of_triangles)

end_time = datetime.now()
print("Execution time:", end_time - start_time)
