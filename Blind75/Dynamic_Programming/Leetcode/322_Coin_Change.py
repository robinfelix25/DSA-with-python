
def minCoin(coins,amount):
    res = float("inf")
    def dfs(coins, target, cur):
        nonlocal res
        if target == amount:
            res = min(res, len(cur))
            return
        if target > amount:
            return
        
        for i in range(len(coins)):
            dfs(coins[i:], target + coins[i], cur + [coins[i]])

    dfs(coins, 0, [])
    return res if res != float("inf") else -1

# not working
def minCoin_memo(coins, amount):
    res = float("inf")
    memo = {}
    min_res = float("inf")
    def dfs(coins, target, cur):
        nonlocal res
        nonlocal memo
        nonlocal min_res
        if target == amount:
            print(cur)
            return len(cur)
        
        if target > amount:
            return
        
        if target in memo: return min(len(cur), memo[target])

        for i in range(len(coins)):
            res = dfs(coins[i:], target + coins[i], cur + [coins[i]])
            if res: 
                min_res = min(res, min_res)
                memo[target] = min_res
                print(target, min_res)
                return memo[target]

    dfs(coins, 0, [])
    print(memo)
    return min_res if min_res != float("inf") else -1

# DP approach
def minCoin(coins, amount):
    dp = [float("inf") for _ in range(amount+1)]
    dp[0] = 0

    for a in range(1,amount+1):
        for c in coins:
            if a-c >=0:
                dp[a] = min(dp[a], 1 + dp[a-c])
    
    return dp[-1] if dp[-1] != float("inf") else -1

# coins = [2]
# amount = 3
# print(coinChange(coins, amount))
# coins = [1,2,5]
# amount = 11
# print(coinChange(coins, amount))

def minCoin_try(coins,amount):
    res = float("inf")
    def dfs(target, cur, memo = {}):
        nonlocal res
        if target in memo:
            return memo[target]
        if target == amount:
            res = min(res, len(cur))
            return res
        if target > amount:
            return 0
        
        for i in range(len(coins)):
            ret = dfs(target + coins[i], cur + [coins[i]], memo)
            memo[target] = ret
            print(memo)
        return ret
        

    dfs(0, [])
    return res if res != float("inf") else -1

coins = [1,3,4,5]
amount = 7
print(minCoin_try(coins, amount))

# amount = 11
print(minCoin_try(coins, amount))

# coins = [2]
# amount = 3
# print(minCoin(coins, amount)) # -1
# coins = [1,2,5]
# amount = 11
# print(minCoin(coins, amount)) # 3

# coins = [1,5]
# amount = 6
# print(minCoin(coins, amount))