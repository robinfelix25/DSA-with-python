from collections import deque

def has_path_dfs_itr(graph, s, d):
    stack = [s]
    while stack:
        cur = stack.pop()
        # print(cur, end='-->')
        if cur == d:
            return True
        for nei in graph[cur]:
            stack.append(nei)
    return False

def has_path_bfs_ite(graph, s, d):
    queue = deque()
    queue.append(s)
    
    while queue:
        cur = queue.popleft()
        # print(cur, end='-->')
        if cur == d:
            return True
        for nei in graph[cur]:
            queue.append(nei)
    return False

def has_path_dfs_rec(graph, s, d):
    if s == d:
        return True
    for nei in graph[s]:
        if has_path_dfs_itr(graph, nei, d):
            return True
    return False

graph = {
    'f' : ['g', 'i'], 
    'g' : ['h'],
    'h' : [],
    'i' : ['g','k'],
    'j' : ['i'],
    'k' : []
}
# graph = { "a" : ["c","b"],
#             "b" : ["d"],
#             "c" : ["e"],
#             "d" : ["f"],
#             "e" : [],
#             "f" : []
#                }
print(has_path_dfs_itr(graph, 'f', 'k'))
print(has_path_bfs_ite(graph, 'f', 'k'))
print(has_path_dfs_rec(graph, 'f', 'k'))