# def binarytree():
#     print ("hello world")


# def 

# coding,
# 4 round

# different aspects of the interview

# l1 = ['r','o','b']

# for i in range(len(l1)):
#     print(len(l1))
#     print(l1.pop())
#     if len(l1) == 1:
#         l1 = l1 + ['i','n']

# print(l1) 


# Threesum in educative.io, Tried simply
# def threesum(nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1

#     for n in nums:
        
#         # print(nums)
#         while l <= r :
#             if n == nums[l] or n == nums[r]:
#                 break
#             threesum = n + nums[l] + nums[r]

#             if threesum < target:
#                 l += 1
#             elif threesum > target:
#                 r -= 1
#             else:
#                 return [n, nums[l], nums[r]]


# input = [3,7,1,2,8,4,5]
# target = 9
# print(threesum(input, target))

# def subsets(nums):
#         res = []

#         subset = []

#         def dfs(i):
#             if i >= len(nums):
#                 res.append(subset.copy())
#                 return
#             # decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i + 1)
#             # decision NOT to include nums[i]
#             subset.pop()
#             dfs(i + 1)

#         dfs(0)
#         return res
        
# nums = [1,2]
# subsets(nums)

# def fib(n):
#     if n in [0,1]:
#         return n
#     else:
#         left = fib(n-2)
#         right = fib(n-1)
#         res = left + right
#         return res
    
# print(fib(4))
# print(1 < 2)
# print (1 in range(10))



# customDict = { "a" : ["b","c"],
#             "b" : ["a", "d", "e"],
#             "c" : ["a", "e"],
#             "d" : ["b", "e", "f"],
#             "e" : ["d", "f", "c"],
#             "f" : ["d", "e"]
#                }



def longest(graph):
    visited = set()
    max_long = 0
    def dfs(graph, node):
        if node in visited:
            return False
        
        visited.add(node)
        length = 1
        for nei in graph[node]:
            length += dfs(graph, nei)
    
        return length
    
    for k in graph:
        if k not in visited:
            long = dfs(graph, k)
            max_long = max(long, max_long)
    return max_long

graph = {
    0 : [8,1,5],
    1 : [0],
    5 : [0, 8],
    8 : [0, 5],
    2 : [3, 4],
    3 : [2, 4],
    4 : [3, 2]
}

print(longest(graph))