# Created By : Robin Felix (buildwithfelix@gmail.com)

def searchMatrix(matrix, target):
    # Thought of having BS as separate function
    def binarysearch(nums, target):
        print ("in BS")
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1

    for row in matrix:
        if row[-1] >= target:
            out = binarysearch(row, target)
            if out >= 0: 
                return True
            
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix, target))