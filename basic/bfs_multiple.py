from collections import deque

def single_bfs(graph, start_node, visited):
    queue=deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(f"Visitng: {current_node}")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return list(visited)


def bfs_disconnected_graph(graph):
    """
    비연결 그래프의 모든 노드를 BFS로 탐색하고 연결 컴포넌트를 반환하는 함수.
    """
    all_visited = set() # 그래프 전체의 방문 기록
    connected_components = [] # 발견된 연결 컴포넌트들을 저장할 리스트

    # 그래프의 모든 노드를 순회
    # 딕셔너리의 키들을 사용하여 모든 노드를 얻을 수 있습니다.
    for node in graph:
        if node not in all_visited:
            # 아직 방문하지 않은 노드라면 새로운 연결 컴포넌트가 시작된 것입니다.
            print(f"\n--- 새로운 컴포넌트 탐색 시작 (시작 노드: {node}) ---")
            component = single_bfs(graph, node, all_visited)
            connected_components.append(component)
            print(f"방문 노드: {component}")

    return connected_components


graph_2_disconnected = {
    '1': ['2', '3'],
    '2': ['1'],
    '3': ['1'],
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}

print("비연결 그래프 전체 BFS 탐색 시작:")
all_components = bfs_disconnected_graph(graph_2_disconnected)

print("\n--- 모든 연결 컴포넌트 ---")
for i, component in enumerate(all_components):
    print(f"컴포넌트 {i+1}: {component}")
