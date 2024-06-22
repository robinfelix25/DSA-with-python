

def minCostClimbingStairs(cost):
    dp = cost[:]
    dp[1] = min(dp[0, dp[1]])
    total = 0
    for i in range(2,len(cost)):
        dp[i] = min(dp[i-1], dp[i-2])
        total += dp[i]

    return total



cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))