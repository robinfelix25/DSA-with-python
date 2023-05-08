

def permute_sol1(nums):
    res = []
    visited = set()

    def dfs(cur):
        if len(cur) == len(nums):
            res.append(cur[:])
            return

        for i, n in enumerate(nums):
            if i not in visited:
                visited.add(i)
                dfs(cur + [n])
                visited.remove(i)
    dfs([])    
    return res

def permute_sol2(nums):
    res = []
    cur = []
    used = [False] * len(nums)

    def dfs(i):
        if len(cur) == len(nums):
            res.append(cur.copy())
            return

        for i, n in enumerate(nums):
            if used[i]:
                continue
            
            cur.append(nums[i])
            used[i] = True
            dfs(i)
            # print(cur)
            cur.pop() 
            used[i] = False
        
    dfs(0)
    return res

nums = [1,2,3]
print(permute_sol1(nums))
print(permute_sol2(nums))