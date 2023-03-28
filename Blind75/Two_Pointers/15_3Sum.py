# Created By : Robin Felix (buildwithfelix@gmail.com)

# TODO:still there are some improments can be done, Need to look into future 

def threeSum(nums):
    nums.sort()

    res = []
    for i, a in enumerate(nums):
        if a > 0:
            break

        #improved code block improved code 
        if i > 0 and a == nums[i - 1]:
                continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            threesum = a + nums[l] + nums[r]

            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                # this code doesnt eliminate duplicates [-1, -1, 0, 1, 2, 4] both -1 will be rechecked again,
                #slight improvement is below
                # if not [a, nums[l], nums[r]] in res:
                #     res.append([a, nums[l], nums[r]])
                res.append([a, nums[l], nums[r]])
                l += 1
                r -= 1

                #slight improvement below, not required if confusing comment and follow above
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            
    return res
nums = [-1, 0,1,2,-1,4]
print(threeSum(nums))



# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]