def dfs_recursive(graph, start_node, visited):
    visited.add(start_node)
    print(f"VisitNode: {start_node}")

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)



graph_1_connected = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#       D
#       |
#       |
# A --- B --- E
# |     |     |
# |     |     |
# C --- F -----

print("--- 재귀 방식 DFS (시작: A) ---") # 7
visited_recursive = set() # 8
dfs_recursive(graph_1_connected, 'F', visited_recursive) # 9



