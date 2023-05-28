

'''
for this kind of DP tabulation problem it really tough to come up with the logic
the pattern need to be found
approach to solve the pattern is tough
'''
def howsum_sol1(targetsum, numbers):
    dp = [None for _ in range(targetsum+1)]
    dp[0] = []

    for i in range(targetsum+1):
        for n in numbers:
            if dp[i] != None and i+n < len(dp):
                dp[i+n] = dp[i] + [n]

    return dp[targetsum]

print(howsum_sol1(7,[5,3,4]))
