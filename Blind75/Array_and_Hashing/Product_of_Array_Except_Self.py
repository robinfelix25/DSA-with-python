# Created By : Robin Felix (buildwithfelix@gmail.com)

#Solution 1: without creating preorder and postorder lists
def productExceptSelf(nums):
    res = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    print(res)

    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

#Solution 2: using preorder and postorder list, space or two lists will increase in this solution
def productExceptSelf2(nums):
    length = len(nums)
    ltor = [1] * len(nums) 
    rtol = [1] * len(nums)

    for l in range(1,length):
        ltor[l] = ltor[l-1] * nums[l-1]
    
    print(ltor)

    for r in range(length - 2, -1, -1):
        rtol[r] = rtol[r+1] * nums[r+1]
    print(rtol)

    for i in range(length):
        nums[i] = ltor[i] * rtol[i]
    
    return nums

nums = [1,2,3,4]
print(productExceptSelf2(nums))

