

'''
This problem is similar to House robber I, But since its circular
its about 
- not including last element or
- not including first element
'''
def houserobberII(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    def rob(nums):
        first, sec = 0, 0

        for n in nums:
            temp = max(n+sec, first)
            sec = first
            first = temp
        
        return first
    
    return max(rob(nums[1:]), rob(nums[:-1]))

print(houserobberII([2,3,2]))