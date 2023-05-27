
# Figured out my solution
def howsum_mysol(nums, target):
    res = []
    def dfs(nums, cur, total):
        if total == target:
            res.append(cur[:])
            return True
        
        if total > target:
            return False
        
        for i, n in enumerate(nums):
            if dfs(nums[i:], cur+[n], total+n):
                return True
        # for i in range(index, len(nums)):
            # need to work on not using same number
            # dfs(i+1, nums[i:], cur+[nums[i]], total+nums[i])
            
        #Return all possible combinations
        # for i, n in enumerate(nums):
        #     dfs(nums, cur+[n], total+n)
            
        return False
    
    dfs(nums, [], 0)
    return res

# tuto approach
def howsum(nums, target, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for n in nums:
        reminder = target - n
        reminderres = howsum(nums, reminder, memo)
        if reminderres != None:
            memo[target] = reminderres + [n]
            return memo[target]
    
    memo[target] = None
    return None
# print(howsum_mysol([5,3,4,7], 7))
# print(howsum_mysol([7, 14], 300))
# print(howsum_mysol([2,5], 8))

print(howsum([5,3,4,7], 7))
print(howsum([7, 14], 300))