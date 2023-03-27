def threeSum(nums):
    nums.sort()

    res = []
    for i, a in enumerate(nums):
        if a > 0:
            break
        l, r = i + 1, len(nums) - 1

        while l < r:
            threesum = a + nums[l] + nums[r]

            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                if not [a, nums[l], nums[r]] in res:
                    res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1
            
    return res
nums = [-1, 0,1,2,-1,4]
print(threeSum(nums))



# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]