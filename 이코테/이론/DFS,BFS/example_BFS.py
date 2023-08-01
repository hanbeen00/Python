from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start] = True 
    
    while queue:
        v=queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




graph=[         #2차원 리스트로 그래프 표현
    [],
    [2 ,3, 8],  #노드 1과 인접한 노드
    [1, 7],     #노드 2와 인접한 노드
    [1, 4, 5],  #노드 3과 인접한 노드
    [3, 5],     #노드 4와 인접한 노드
    [3, 4],     #노드 5와 인접한 노드
    [7],        #노드 6과 인접한 노드
    [2, 6, 8],  #노드 7과 인접한 노드
    [1, 7]      #노드 8과 인접한 노드
]

visited = [False] * 9   #각 노드 방문여부(초기값: 방문x)

bfs(graph,1,visited)
