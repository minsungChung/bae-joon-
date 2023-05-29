n = int(input())
graph = []
visited = [0]*n
result = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(start, end, visited):

    for i in range(n):
        if graph[start][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i, end, visited)
            
    if visited[end] == 1:
        return 1
    else:
        return 0


for i in range(n):
    tmp = []
    for j in range(n):
        visited = [0]*n
        tmp.append(dfs(i, j, visited))
    result.append(tmp)


for row in result:
    for ele in row:
        print(ele, end = ' ')
    print()