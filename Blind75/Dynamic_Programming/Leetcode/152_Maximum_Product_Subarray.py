
def maxProduct(nums):
    res = []
    def dfs(idx, nums, cur):
        res.append(cur)
        for i in range(idx,len(nums)):
            dfs(i+1, nums[i:], cur + [nums[i]])
    dfs(0, nums, [])
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))