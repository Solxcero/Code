import sys

input = sys.stdin.readline

N, M, V = map(int,input().split())
graph = {}
gp = []
for i in range(1,N+1):
    graph[i] =[]
for _ in range(M):    
    a,b = list(map(int,input().split()))
    gp.append([a,b])
    graph[a] += [b]
    graph[a].sort()
    graph[b] += [a]
    graph[b].sort()
# graph = sorted(graph)

def bfs(graph, start_node):
    from collections import deque
    visited = []
    need_visit = deque()
    
    ##시작 노드 
    need_visit.append(start_node)
    
    ## 방문이 필요 노드 존재시 실행
    while need_visit:
        ## 시작 노드를 지정
        node = need_visit.popleft()
        # print(f'시작노드: {node}')
 
        if node not in visited: 
            visited.append(node)
            print(node,end=' ')
            # print(f'방문 노드 : {visited}')
            ## 해당 노드들 -> need_visited에 추가 
            need_visit.extend(graph[node])
            # print(f'방문 필요 노드 : {need_visit}')
            
    # return visited
    return
    # for i in visited:               
    #     print(i, end=' ')
    

def dfs(graph, start_node):
    from collections import deque
    visited = []
    need_visit = deque()
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        # print(f'시작노드: {node}')
 
        if node not in visited:
 
            visited.append(node)
            # print(f'방문 노드 : {visited}')
            
            need_visit.extend(reversed(graph[node]))
            # print(f'방문 필요 노드 : {need_visit}')
     
    # return visited
    for i in visited:               
        print(i, end=' ')
    print()

# print(graph)
dfs(graph,V)
bfs(graph,V)

