
# time: o(n) ; space: o(n)
def maxSubsetSumNoAdjacent_sol1(array):
    # Write your code here.
    dp = array[:]
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]

    dp[1] = max(dp[0], dp[1])
    for i in range(2,len(array)):
        dp[i] = max(dp[i-1], dp[i-2] + array[i])

    return dp[-1]

def maxSubsetSumNoAdjacent_sol2(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    
    first = max(array[0], array[1])
    second = array[0]
    current = 0
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        first, second = current, first
    
    return first
array = [75, 105,120,75,90,135] # 75+120+135
print(maxSubsetSumNoAdjacent_sol1(array))
print(maxSubsetSumNoAdjacent_sol2(array))