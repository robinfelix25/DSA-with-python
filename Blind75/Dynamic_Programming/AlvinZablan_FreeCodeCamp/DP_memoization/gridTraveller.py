

def gridtraveller(r, c, memo = {}):
    if r == 0 or c ==0 : return 0
    if r == 1 and c == 1: return 1
    if (r,c) in memo: return memo[(r,c)]
    memo[(r,c)] = gridtraveller(r-1, c) + gridtraveller(r, c-1)
    return memo[(r,c)]

print(gridtraveller(2,3))
print(gridtraveller(18,18)) # Applied memoization for this test case
print(gridtraveller(200,300)) # Applied memoization for this test case
