import networkx as nx
import numpy as np
# import matplotlib.pyplot as plt

# Create the graph G
G = nx.Graph()
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
edges = [(1, 2), (1, 9), (1, 10), (2, 7), (2, 9), (3, 8), (3, 10), (4, 8),
         (4, 11), (5, 7), (5, 8), (5, 9), (5, 11), (5, 12), (6, 9),
         (7, 10), (7, 8), (8, 10), (8, 11), (11, 12)]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# ------------------- Calculate the shift factor matrix ------------------- #
# Calculate the incidence_matrix
incidence_matrix = nx.incidence_matrix(G, oriented=True).toarray()
# Calculate the laplacian_matrix and take its inverse
laplacian_matrix = nx.laplacian_matrix(G).toarray()
lp_inverse = np.linalg.pinv(laplacian_matrix)
# transpose of the incidence matrix
V = -np.matmul(incidence_matrix.T, lp_inverse)
print(V)
np.savetxt("V_shift_factor_matrix.csv", V, delimiter=",", fmt='%f')

# ------------------- Visualize the graph ------------------- #
# node_colors = {1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue',
#                6: 'red', 7: 'red', 8: 'red', 9: 'red', 10: 'red'}
# node_positions = {1: (0.4, 1.4), 2: (1, 0.8), 3: (2.3, 2.3), 4: (3.3, 1.5),
#                   5: (1.9, 0.1), 6: (3.4, 0.5), 7: (1.5, 1.1), 8: (2.4, 1.4),
#                   9: (0.6, 0.4), 10: (1.5, 1.7)}


# # Set node colors and positions
# node_colors = [node_colors[node] for node in G.nodes]
# node_positions = {node: node_positions[node] for node in G.nodes}

# # Draw the graph, needs matplotlib
# nx.draw(G, with_labels=True, node_color=node_colors, pos=node_positions)
# plt.show()

