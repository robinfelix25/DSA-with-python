

# Solution using dp table
def houserobber_sol1(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    dp = nums[:]
    dp[1] = max(nums[0], nums[1])

    for i in range(2,len(nums)):
        dp[i] = max( dp[i-1], nums[i] + dp[i-2] )

    return dp[-1]

print(houserobber_sol1([75, 105,120,75,90,135]))

#Solution with last two variables, # most optimized solution so far
def houserobber_sol2(nums):
    # first = max(nums[1], nums[0])
    # sec = nums[0]
    first , sec = 0, 0 # this is best way to do it, But takes some time to digest

    for n in nums:
        temp = max(n+sec, first)
        sec = first
        first = temp
    
    return first

print(houserobber_sol1([75, 105,120,75,90,135]))
print(houserobber_sol1([1]))

