

# def subs(s):
#     res = []
#     def dfs(idx, cur):
#         # res[cur[:]] = len(cur[:])
#         res.append(cur[:])
#         # if idx >= len(s):
#         #     res.append(cur[:])
#         #     return

#         for i in range(idx, len(s)):
#             dfs(i+1, cur + s[i])

#     dfs(0,'')
#     res = max(res, key=len)
#     return res

# print(subs('abc'))

# # def longestPalindrome(s):
