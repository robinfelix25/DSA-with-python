visited = set()
def undirectedPath(edges, src, dest):
    graph = buildgraph(edges)
    return haspath(graph, src, dest)

#check is the path is available
def haspath(graph, src, dest):
    global visited
    # print(visited)
    if src == dest:
        return True
    if src in visited:
         return False
    
    visited.add(src)
    
    for nei in graph[src]:    
        if haspath(graph, nei, dest):
            return True
    return False

# Convert edges to graph (undirected graph)
def buildgraph(edges):
    graph = {}

    for r, l in edges:
        if r not in graph: graph[r] = []
        if l not in graph: graph[l] = []
        graph[r].append(l)
        graph[l].append(r)
    
    print(graph)
    return graph

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
# buildgraph(edges)

print(undirectedPath(edges, 'i', 'o')) #False
visited = set()
print(undirectedPath(edges, 'i', 'm')) #True