
def rec(n, memo = {}):
    if n in memo: return memo[n]
    if n in [0,1]:
        return n
    res = rec(n-1) + rec(n-2)
    memo[n] = res
    return res

def rec1(n):
    if n in [0,1]:
        return n
    return rec1(n-1) + rec1(n-2)

def rec2(n):
    first = 0
    second = 1
    
    for i in range(n):
        first, second = first+second , first
    
    return first

print(rec(700))
print(rec1(700))
print(rec2(6000))