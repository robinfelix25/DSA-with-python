

def components(graph):
    visited = set()
    count = 0
    def dfs(graph, node):
        if node in visited:
            return False
        visited.add(node)

        for nei in graph[node]:
            dfs(graph, nei)


    for k in graph:
        if k not in visited:
            dfs(graph, k)
            count += 1

    return count

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