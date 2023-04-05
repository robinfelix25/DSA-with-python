
"""
My solution some of the corner cases are failing
"""
def search(nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)// 2
            if nums[m] == target:
                return m
            if nums[m] > nums[r] and nums[m] > target:
                    l = m + 1
            else:
                r = m - 1
        return -1

nums = [4,5,6,7,0,1,2]
nums = [1,3]
target = 3
print(search(nums, target))