
def possiblewords(letters, n):
    res = []

    def dfs(i, path):
        if i == n:
            res.append(''.join(path))
            return
        
        for l in letters:
            path.append(l)
            dfs(i + 1, path)
            path.pop()
        
    dfs(0, [])
    return res


letters = ['a','b']
print(possiblewords(letters, len(letters)))



# res = []
#         def dfs(idx, path):
#             res.append(path.copy())
#             for i in range(idx, len(nums)):
#                 path.append(nums[i])
#                 dfs(i+1, path)
#                 path.pop()
#         dfs(0, [])
#         return res
