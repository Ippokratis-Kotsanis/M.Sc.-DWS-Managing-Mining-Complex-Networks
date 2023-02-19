# All triplets, brute force

from datetime import datetime
import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd

start_time = datetime.now()

df = pd.read_csv("lastfm_asia_edges.csv")
G = nx.from_pandas_edgelist(df, source='node_1', target='node_2')
# G = nx.lollipop_graph(4, 6)
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
# nx.draw(G, with_labels=True)
# plt.show()

end_time = datetime.now()
print("Execution time:", end_time - start_time)
