

# Bottom up approach memoization
def fibmemo(n, memo):
    if n in [1,2]:
        return n
    
    if n not in memo:
        # memo[n] = fibdp(n-1, memo) + fibdp(n-2, memo)
        # for better understanding
        left = fibmemo(n-1, memo)
        right = fibmemo(n-2, memo)
        memo[n] = left + right

    return memo[n]

print(fibmemo(6, {}))

# TOP down approach tabulation

def fibtab(n):
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    print(tb)
    return tb[n-1]

print(fibtab(6))