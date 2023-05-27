


# Tried something on my own, using backtracking
def cansum_try(nums, target):

    def dfs(nums, total):
        if total == target:
            return True
        if total > target:
            return False
        
        for i, n in enumerate(nums):
            if dfs(nums[i:], total + n):
                return True
        return False
    
    return dfs(nums, 0)

# actual tuto code
def cansum(target, nums, memo = {}):
    if target in memo: return memo[target]
    if target < 0: return False
    if target == 0: return True

    for n in nums:
        reminder = target - n
        if cansum(reminder, nums):
            memo[target] = True
            return True
    
    memo[target] = False
    return False
nums = [5,3,4,7]
target = 7
# print(cansum_try(nums, target))
# print(cansum_try([7, 14], 300))

print(cansum(7, [5,3,4,7]))
print(cansum(300, [7, 14]))