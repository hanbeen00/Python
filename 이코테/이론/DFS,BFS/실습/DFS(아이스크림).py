def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: #범위 밖 노드일 경우
        return False

    if graph[x][y] == 0: #방문 안한 노드일 경우
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    
    return False #방문 노드거나 원래 1인 노드



#입력 받을 경우
'''n, m =map(int, inpput().split)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))'''

#입력 x, 바로 초기화
graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]

n = 4
m = 5

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result = result+1

print(result)


        

    
