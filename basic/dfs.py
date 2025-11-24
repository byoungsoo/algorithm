from collections import deque


def dfs(graph, start_node):
    visited = set()
    queue=deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.pop()            # 이 부분이 Last In First Out ( LIFO ) 가 되면서 깊이 우선 탐색을 실행하게 됨.
        print(f"Visitng: {current_node}")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph_1_connected = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

graph = [
    [],
    [2,3,7],
    [1,4,6],
    [1,5, 7],
    [2,6],
    [3,7],
    [2,4],
    [1,3]
]


visit_list1 = dfs(graph_1_connected, 'A')
print("---------")
visit_list2 = dfs(graph, 1)

print(visit_list1)
print(visit_list2)