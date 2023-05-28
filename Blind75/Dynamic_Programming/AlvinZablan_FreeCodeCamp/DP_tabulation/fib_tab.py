# Version 1
def fib_tab_sol1(n):
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(fib_tab_sol1(6))

# Version 2
def fib_tab_sol2(n):
    dp = [0,1]
    for i in range(2,n+1): # Notice we are cal extra one value to manage list out of index
        dp.append(dp[i-1]+dp[i-2])

    return dp[n]

print(fib_tab_sol2(6))
print(fib_tab_sol2(50))

# Version 3
def fib_tab_sol3(n):
    first = 1
    second = 0 

    for i in range(2,n+1):
        first, second = first+second, first

    return first

print(fib_tab_sol3(6))
print(fib_tab_sol3(50))