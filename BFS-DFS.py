# Find all paths starting from 'CP'
all_paths_from_cp_dfs = find_paths_dfs(G, 'CP')

# Print all paths starting from 'CP'
print("DFS Paths:")
for path in all_paths_from_cp_dfs:
    print(" -> ".join(path))

print("\n")
# Find all paths starting from 'CP'
all_paths_from_cp_bfs = find_paths_bfs(G, 'CP')

print("BFS Paths:")
# Print all paths starting from 'CP'
for path in all_paths_from_cp_bfs:
    print(" -> ".join(path))


# Function to perform DFS and find all paths starting from 'CP'
def find_paths_dfs(graph, start_node, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Mark the current node as visited and add to the path
    visited.add(start_node)
    path.append(start_node)

    # If there are no more neighbors, return the path
    if len(list(graph.neighbors(start_node))) == 0:
        return [path]

    paths = []
    for neighbor in graph.neighbors(start_node):
        if neighbor not in visited:
            new_paths = find_paths_dfs(graph, neighbor, visited.copy(), path.copy())
            paths.extend(new_paths)
    return paths


# Function to perform BFS and find all paths starting from 'CP'
def find_paths_bfs(graph, start_node):
    # Queue for BFS (holds the current path to be explored)
    queue = deque([[start_node]])
    paths = []

    while queue:
        path = queue.popleft()  # Get the current path
        node = path[-1]  # Get the last node from the path

        # Maintain a set of visited nodes to avoid revisiting them in the same path
        visited = set(path)  # Visited nodes for the current path

        # Check for neighbors (outgoing edges)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:  # Only explore unvisited neighbors
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)  # Add the new path to the queue

                # If the neighbor has no outgoing edges, add the path to all_paths
                if len(list(graph.neighbors(neighbor))) == 0:
                    paths.append(new_path)
    return paths