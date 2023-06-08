
# back tracking brute force, still can be improved
def stairs(n):
    count = 0
    def dfs(res, memo = {}):
        nonlocal count
        if res in memo: return memo[res]
        if res == n:
            count +=1
            return True
        if res > n:
            return False
        
        memo[res] = 0
        for i in [1,2]:
            ret = dfs(res + i, memo)
            memo[res+i] = ret
            # print(ret)
        print(memo)
    dfs(0)
    return count

n = 3
# print(stairs(n))


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

def claimstairs_sol1(n, memo = {}):
    if n in memo: return memo[n]
    if n == 0: return 1
    if n < 0 : return 0

    count = 0
    for i in [1,2]:
        noofways = claimstairs_sol1(n-i, memo)
        count += noofways
        memo[n] = count
    return count

print(claimstairs_sol1(3))

# print(climbstairs(3))

# Solve in DP

# def claimstairs_tab(n):
#     dp