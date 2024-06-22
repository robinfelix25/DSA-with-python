
'''
Interesting DP problem to start with 
'''
# back tracking brute force, still can be improved
def stairs(n):
    count = 0
    def dfs(res, memo = {}):
        nonlocal count
        if res in memo: return memo[res]
        if res == n: return 1 
        if res > n: return 0
        
        for i in [1,2]:
            ret = dfs(res + i, memo)
            if ret:
                count += ret
                memo[res] = count 
        # print(memo)
    dfs(0)
    return count

n = 3
print(stairs(n))


# same as above tried with different template
def climbstairs(n):
    count = 0
    def dfs(res):
        nonlocal count
        if res == n:
            count += 1
            return
        
        if res > n:
            return
        
        dfs(res + 1)
        dfs(res + 2)
    dfs(0)
    return count


# recursive with memo techique
def claimstairs_memo(n, memo = {}):
    if n in memo: return memo[n]
    if n == 0: return 1
    if n < 0 : return 0

    count = 0
    for i in [1,2]:
        noofways = claimstairs_memo(n-i, memo)
        count += noofways
        memo[n] = count
    return count

print(claimstairs_memo(3))


# Dp approach with complete table in place, more space required
def claimstairs_tab(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

print(claimstairs_tab(3))

# Full optimized dp approach with, two variables instead of storing the entire table
def claimstairs_full_dp(n):
    first = 1
    sec = 1

    for i in range(n-1):
        # first, sec = first + sec, sec
        temp = first
        first = first + sec
        sec = temp
    
    return first

print(claimstairs_full_dp(3))
