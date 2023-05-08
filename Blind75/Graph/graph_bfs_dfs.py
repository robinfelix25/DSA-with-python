
from collections import deque

def itr_dfs(graph, node):
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)
        for nei in graph[node]:
            stack.append(nei)

def itr_bfs(graph, node):
    queue = deque(node)

    while queue:
        node = queue.popleft()
        print(node)
        for nei in graph[node]:
            queue.append(nei)

def rec_dfs(graph, node):
    print(node)
    for nei in graph[node]:
        rec_dfs(graph, nei)

graph = { "a" : ["c","b"],
            "b" : ["d"],
            "c" : ["e"],
            "d" : ["f"],
            "e" : [],
            "f" : []
               }
# itr_dfs(graph, 'a')
# rec_dfs(graph, 'a')

itr_bfs(graph, 'a')


