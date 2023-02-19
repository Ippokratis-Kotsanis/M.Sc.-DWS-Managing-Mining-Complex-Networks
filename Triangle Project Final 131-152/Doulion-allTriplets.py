# Doulion & allTriplets

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

# Add all-triplets algorithm
edgeList = G.edges()
triangles = list()
trianglePair = list()
list_of_lists_edgelist = [list(edge) for edge in edgeList]
# The following program will simply go through the list
# of edges, check if they have a common point and if they do, it will check if
# the remaining two points also constitute an edge in the input set.
for i in range(0, len(list_of_lists_edgelist)-1):
    for j in range(0, len(list_of_lists_edgelist) - 1):
        indices_to_access = [i, j + 1]
        accessed_mapping = map(list_of_lists_edgelist.__getitem__, indices_to_access)
        accessed_list = list(accessed_mapping)
        e1 = tuple(accessed_list[0])
        e2 = tuple(accessed_list[1])
        if e1[0] == e2[0]:
            if (e1[1], e2[1]) in edgeList:
                trianglePair.append(e1[0])
                trianglePair.append(e1[1])
                trianglePair.append(e2[1])
                triangles.append(sorted(tuple(trianglePair)))
                trianglePair.clear()
triangles_set = list(set(map(tuple, triangles)))  # remove duplicate triangles
print("Triangles are:", triangles_set)
number_of_triangles = len(triangles_set)
print("Number of triangles:", number_of_triangles)
My_real_number_of_trinagles = number_of_triangles * ((1/p)**3)
print("Final number of triangles", My_real_number_of_trinagles)
# nx.draw(G, with_labels=True)
# plt.show()

end_time = datetime.now()
print("Execution time:", end_time - start_time)





