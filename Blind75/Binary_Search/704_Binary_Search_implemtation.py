
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        # m = l + (r - l) // 2 # This is complex in other programing lang it may lead to over flow
        m = (l+r) // 2
        print(nums, m)
        if target > nums[m]:
            l = m + 1
        elif target <  nums[m]:
            r = m - 1
        else:
            return m
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums, target))