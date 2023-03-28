
def maxArea(height):
    l,  r = 0, len(height) - 1
    max_area = 0
    while l < r:
        area = ((r+1) - (l+1)) * min(height[l], height[r])
        max_area = max(max_area, area)
 
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height)) #runtime: 2155 ms

#TODO Need to improve this solution
