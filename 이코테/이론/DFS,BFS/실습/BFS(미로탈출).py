from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))
                
    return graph[n-1][m-1]


#입력 받을 경우
'''n, m =map(int, inpput().split)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))'''

#입력 x, 바로 초기화
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

n = 5
m = 6

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
