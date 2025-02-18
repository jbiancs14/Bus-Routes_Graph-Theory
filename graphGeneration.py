import networkx as nx
import matplotlib.pyplot as plt

# Create a directed multigraph to allow multiple edges
G = nx.MultiDiGraph()

# Edges (including weights)
weighted_edges1 = [("CP", "CL", 6), ("CL", "CVL", 2), ("CVL", "SML", 6), ("SML", "SCL", 2),
                   ("SCL", "WR", 2), ("WR", "SKYO", 2), ("SKYO", "GSS", 2)]
weighted_edges2 = [("CP", "FH", 4), ("FH", "SH", 2), ("SH", "BRNS", 2), ("BRNS", "FG", 3), ("FG", "BBB", 2),
                   ("BBB", "CW", 1), ("CW", "HL", 1), ("HL", "LG", 1), ("LG", "IG", 5),
                   ("IG", "QL", 5), ("QL", "NVRC", 3), ("NVRC", "UNL", 3), ("UNL", "SCC", 2),
                   ("SCC", "CG", 2), ("CG", "DP", 2)]
weighted_edges3 = [("CP", "CG", 3), ("CG", "WL", 2), ("WL", "WA", 2), ("WA", "UNL", 1), ("UNL", "NVRC", 2),
                   ("NVRC", "QL", 2),
                   ("QL", "BBB", 4), ("BBB", "CW", 1), ("CW", "HL", 1), ("HL", "IG", 5), ("IG", "SDL", 1),
                   ("SDL", "BRNS", 3), ("BRNS", "SIMS", 1), ("SIMS", "FH", 5),
                   ("FH", "SH", 5)]
weighted_edges4 = [("CP", "CW", 2), ("CW", "STG", 3), ("STG", "PH", 5), ("PH", "WHS", 5)]
weighted_edges5 = [("CP", "GI", 7), ("GI", "GC", 1), ("GC", "GW", 4), ("GW", "WE", 4)]

# Define the bus routes as separate subnetworks
routes = {
    'Red Line': weighted_edges1,
    'Blue Line': weighted_edges2,
    'Green Line': weighted_edges3,
    'Yellow Line': weighted_edges4,
    'Brown Line': weighted_edges5
}

# Define route colors
route_colors = {'Red Line': 'red', 'Blue Line': 'blue', 'Green Line': 'green', 'Yellow Line': 'gold',
                'Brown Line': 'brown'}

# Add edges to the graph with weight and route attributes
for route, edges in routes.items():
    for u, v, w in edges:
        G.add_edge(u, v, weight=w, route=route, color=route_colors[route])

# Compute positions for nodes
pos = nx.spring_layout(G, seed=42, k=3.0, scale=5)

# Increase/Decrease figure size to make it look better
plt.figure(figsize=(25, 20))

# Draw nodes...feel free to play around with the color and node size
nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=1000)

# Do not change this...it draws the graph
for (u, v, key, data) in G.edges(keys=True, data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color=[data['color']],
                           connectionstyle=f"arc3,rad={0.3 * (key + 1)}",
                           arrowstyle='-|>',
                           min_source_margin=15, min_target_margin=15,  # Ensures arrows don't enter nodes
                           arrowsize=15, width=2)

# Add edge weights
edge_labels = {(u, v): data["weight"] for u, v, k, data in G.edges(keys=True, data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='black')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=14, font_color='black', font_weight='bold')

# Show the graph
plt.title("Bus Route Network with Directed Multi-Edges & Weights", fontsize=16)
plt.show()