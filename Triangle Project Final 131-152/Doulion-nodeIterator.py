# Doulion & nodeIterator

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

# Add node-iterator algorithm
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
number_of_triangles = len(triangles_set)
print("Number of triangles:", number_of_triangles)
My_real_number_of_trinagles = number_of_triangles * ((1/p)**3)
print("Final number of triangles", My_real_number_of_trinagles)

end_time = datetime.now()
print("Execution time:", end_time - start_time)





