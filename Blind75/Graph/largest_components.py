

def components(graph):
    visited = set()
    max_len = 0
    def dfs(graph, node):
        if node in visited:
            return 0
        visited.add(node)
        length = 1
        # print(111)
        for nei in graph[node]:
            length += dfs(graph, nei)
        
        return length

    for k in graph:
        if k not in visited:
            long = dfs(graph, k)
            print(long)
            max_len = max(max_len, long)
            
    return max_len

graph = {
    0 : [8,1,5],
    1 : [0],
    5 : [0, 8],
    8 : [0, 5],
    2 : [3, 4],
    3 : [2, 4],
    4 : [3, 2]
}
# buildgraph(edges)

print(components(graph))