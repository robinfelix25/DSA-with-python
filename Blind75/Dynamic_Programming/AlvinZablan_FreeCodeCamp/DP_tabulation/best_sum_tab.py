
def best_sum_sol1(targetsum, numbers):
    res = []
    def dfs(total, cur, memo = {}):
        nonlocal res
        if total in memo: return memo[total]
        if total == targetsum:
            if len(res) == 0 or len(cur) < len(res): # added 
                res = cur[:]
                memo[total] = cur[:]
            return None
        if total > targetsum:
            return None
        
        for n in numbers:
            dfs(total + n, cur + [n], memo)
        return memo[total]
    dfs(0,[])
    return res



def best_sum(targetsum, numbers):
    if targetsum == 0: return []
    if targetsum < 0: return None

    shortestcombination = None

    for n in numbers:
        reminder = targetsum - n
        remindercombination = best_sum(reminder, numbers)
        if remindercombination != None:
            combination = remindercombination + [n]
            print(combination)
            if shortestcombination is None or len(combination) < len(shortestcombination):
                shortestcombination = combination

    
    return shortestcombination

def best_sum_tab(targetsum, numbers):
    dp = [None for _ in range(targetsum+1)]
    dp[0] = []
    for i in range(targetsum+1):
        if dp[i] != None:
            for n in numbers:
                if i+n < len(dp):
                    if dp[i+n] == None or len(dp[i+n]+[n]) < len(dp[i+n]):
                        dp[i+n] = dp[i] + [n]

    return dp[targetsum]


# print(best_sum_tab(7,[5,3,4,7]))
print(best_sum_tab(8, [2,3,5]))
print(best_sum_tab(100, [1,2,5,25]))
print(best_sum_tab(100, [25,2,5,1]))


# print(best_sum_sol1(7,[5,3,4,7]))
# print(best_sum_sol1(8, [2,3,5]))
# print('**',best_sum_sol1(8,[1,4,5]))
# print(best_sum_sol1(100, [1,2,5,25]))
    