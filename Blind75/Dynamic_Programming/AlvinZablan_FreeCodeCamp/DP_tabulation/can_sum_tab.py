

# My Version in this can give parameter 10000, even with memo is not possible. bcz of recursiion size 
# Going for tabulation now
def cansum(targetsum, numbers):
    memo = {}
    def dfs(target):
        nonlocal memo
        if target in memo: return memo[target]
        if target == targetsum:
            return True
        if target > targetsum:
            return False
        
        for n in numbers:
            res = dfs(target+n)
            if res:
                memo[target] = True
                return True
        memo[target] = False
        return False
    
    return dfs(0)

print(cansum(300, [7, 14]))
# print(cansum(10000, [5,3,4])) # Even with memo this is not possible

# DP with tabulation
def cansum_sol2(targetsum, numbers):
    dp = [False for _ in range(targetsum+1)]
    dp[0] = True

    for i in range(targetsum+1):
        for n in numbers:
            if dp[i] == True and i+n < len(dp):
                dp[i+n] = True

    return dp[targetsum]

print(cansum_sol2(7, [5,3,4]))
print(cansum_sol2(300, [7,14]))