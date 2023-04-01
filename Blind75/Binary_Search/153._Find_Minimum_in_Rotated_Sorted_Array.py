
"""
Interesting catch in here is the cur_min, bcz even if the m is in least element, we  dont know its 
least element or not
So we need to maintain a variable to keep track of the min value
"""
def findMin(nums):
    l, r = 0, len(nums) - 1
    cur_min = float("inf")

    while l <= r:
        m = ( l + r ) // 2
        print(m, l, r)
        cur_min = min(cur_min, nums[m])

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return min(nums[m], cur_min)

nums = [3,4,5,1,2]
# nums= [4,5,6,7,0,1,2]
# nums=  [11,13,15,17]
nums = [3,1,2]
print(findMin(nums))