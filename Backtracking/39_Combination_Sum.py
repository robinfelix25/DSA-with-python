
'''
same as the implementation of Subsets

Solution 2 is more relavent for interview
'''

def combinationSum_sol1(candidates, target):
    res = []

    def dfs(nums, cur, total):
        if total == target:
            res.append(cur[:])
            return

        if total > target:
            return

        for i, n in enumerate(nums):
            cur.append(n)
            dfs(nums[i:], cur, total + n)
            cur.pop()

    dfs(candidates, [], 0)
    return res

def combinationSum_sol2(candidates, target):
    res = []

    def dfs(nums, cur, total):
        if total == target:
            res.append(cur[:])
            return

        if total > target:
            return

        for i, n in enumerate(nums):
            dfs(nums[i:], cur + [n], total + n)

    dfs(candidates, [], 0)
    return res

def combinationSum_sol3(candidates, target):
    res = []
    cur = [] 
    def dfs(i, total):
        if target == total:
            res.append(cur.copy())
            return 
        
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, total + candidates[i])

        cur.pop()
        dfs(i + 1, total)
    
    dfs(0, 0)
    return res
candidates = [2,3,6,7]
target = 7
# candidates = [2,3,5]
# target = 8
print(combinationSum_sol1(candidates, target))
print(combinationSum_sol2(candidates, target))
print(combinationSum_sol3(candidates, target))