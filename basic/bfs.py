from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue=deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()  # 이 부분이 First In First Out ( FIFO ) 가 되면서 너비 우선 탐색을 실행하게 됨.
        print(f"Visitng: {current_node}")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return list(visited)




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


bfs(graph_1_connected, 'A')