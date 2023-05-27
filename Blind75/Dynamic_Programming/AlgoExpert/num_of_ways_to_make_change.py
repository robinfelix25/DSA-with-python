

# My solution Just backtracking, need to memoize it
# here coins[i:] solved the issue need to look how it works
def coinChangedfs(coins, amount):
    res = 0
    def dfs(coins, target, cur):
        nonlocal res
        if target == amount:
            # print(cur)
            res += 1
            return 
        
        if target > amount:
            return 
        
        # print(coins)
        for i in range(len(coins)):
            dfs(coins[i:], target + coins[i], cur + [coins[i]]) 
            # here coins[i:] solved the issue need to look how it works
        
    dfs(coins, 0, [])
    return res if res else -1


coins = [2]
amount = 3
print(coinChangedfs(coins, amount)) # -1
coins = [1,2,5]
amount = 11
print(coinChangedfs(coins, amount)) # 11
coins = [1,5]
amount = 6
print(coinChangedfs(coins, amount)) # 2

# tuto solution dp tabulation
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    dp = [1] + [0 for _ in range(n)]

    for coin in denoms:
        for amt in range(1, n + 1):
            if amt >= coin:
                dp[amt] += dp[amt-coin]
    return dp[-1]

print(numberOfWaysToMakeChange(6,[1,5])) #2