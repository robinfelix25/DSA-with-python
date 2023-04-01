
import math


### Solution 1: Brute force solution, not efficient, time limit exceeded
def minEatingSpeed(piles, h):
    
    max_k = 0
    for k in range(1,max(piles)+1):
        total_ate = 0
        for p in piles:
            print(math.ceil(p / k))
            total_ate += math.ceil(p / k)

        if total_ate <= h: 
            return k
 
def minEatingSpeedBinary(piles, h):
    l, r = 1, max(piles)
    res = max(piles)
    while l <= r:
        k = ( l + r ) // 2
        total_time = 0
        for p in piles:
            total_time += math.ceil(p / k)
        
        if total_time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res

piles = [3,6,7,11]
h = 8
# print(minEatingSpeed(piles, h))

print(minEatingSpeedBinary(piles, h))