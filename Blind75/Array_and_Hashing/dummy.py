# Created By : Robin Felix (buildwithfelix@gmail.com)

# import collections
# def something(strs):
#     ans = collections.defaultdict(list)
#     # ans

#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         ans[tuple(count)].append(s)
#         # print(ans.values())

# strs = ["eat","tea","tan","ate","nat","bat"]
# something(strs)

#Interesting concept here: like negative indexing it means we can stop the array where we want to
some = list(range(0,5))
print(some)
print(some[:-2])