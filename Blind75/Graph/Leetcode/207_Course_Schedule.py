
def canFinish(numCourses, prerequisites):
        preMap = {i: [] for i in range(numCourses)}
        visited = set()
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(node):
            if node in visited:
                return False
            if preMap[node] == []:
                return True

            visited.add(node)
            for nei in preMap[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True

        for k in range(numCourses):
            if not dfs(k): return False

        return True

numCourses = 5
prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]] # True

numCourses = 2
prerequisites = [[1,0],[0,1]] # False
print(canFinish(numCourses, prerequisites)) 