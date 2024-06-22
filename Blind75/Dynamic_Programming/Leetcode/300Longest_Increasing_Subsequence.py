
# My solution , memory limit exceeded
def helper(sub):
    status = True
    for i in range(len(sub)):
        if i+1 < len(sub) and sub[i] >= sub[i+1]:
            status = False
    return status

def lengthOfLIS(nums):
    res = []
    max_l = 0
    def dfs(index, cur):
        res.append(cur)

        for i in range(index, len(nums)):
            dfs(i + 1, cur + [nums[i]])
    
    dfs(0, [])
    for cur in res:
        if helper(cur):
            print(cur)
            max_l = max(max_l, len(cur))
    return max_l

nums = [2,5,3,7,101,18]
# nums= [7,7,7,7,7,7,7]
# print(lengthOfLIS(nums))


def lengthOfLIS_sol1(nums):
    res = []
    def dfs(index, cur):
        res.append(cur[:]) 
        
        for i in range(index, len(nums)):
            if i + 1 < len(nums) and nums[i+1] > nums[i]:
                dfs(i+1, cur + [nums[i]])

    dfs(0, [])
    return res

nums = [1,2,4,3]
print(lengthOfLIS_sol1(nums))