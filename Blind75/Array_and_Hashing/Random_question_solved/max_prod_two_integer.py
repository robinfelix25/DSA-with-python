

def maxprod(nums):
    prod = 1
    for l in range(len(nums)):
        for r in range(l+1, len(nums)):
            prod = max(prod ,(nums[l] * nums[r]))
            

    return prod

nums = [1,4,2,3]
print(maxprod(nums))
