
def gridtraveller(m, n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)] # this is better with diff mem, Pythonic way
    # dp = [[0] * (n + 1)] * (m+1) # This occupies the same memory, so changing one will affect other

    dp[1][1] = 1 # This is the trick here, bcz cant travel in (1,1) grid
    
    for i in range(m+1):
        for j in range(n+1):
            if i+1 <= m: dp[i+1][j] += dp[i][j]
            if j+1 <= n: dp[i][j+1] += dp[i][j]

    print(dp)
    return dp[m][n]



print(gridtraveller(3,3))