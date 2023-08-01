def dfs(graph, v, visited):
    visited[v] = True   #현재 노드는 방문처리
    print(v, end=' ')   #방문한 노드 출력

    for i in graph[v]:
        if not visited[i]:  #인접 노드 중 방문 안한 노드
            dfs(graph,i,visited)




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

dfs(graph,1,visited)
