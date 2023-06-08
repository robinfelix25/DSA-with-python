

#Solution got from tuto
# def numDecodings(s):
#     def decode(s, idx, n):
#         if (idx < n and s[idx] == '0'): return 0
#         if (idx >= n):
#             return 1
        
#         ways = 0

#         #Pick Single
#         if (s[idx] != '0'): 
#             ways = decode(s, idx+1, n)
            
#         #Pick Couple
#         if (idx+1 < n and ((s[idx] == '1' and s[idx+1] <= '9') or 
#             (s[idx]=='2' and s[idx+1] < '7'))):
#             ways += decode(s, idx+2, n)

#         return ways

#     n = len(s)
#     return decode(s, 0, n)

# print(numDecodings("12"))


# def numDecodings(nums):
#     res = []

#     def dfs(n):
        
#         dfs()
        

#     dfs(0, '')
#     return res


def numDecodings(s):

    def dfs(i):
        # if i in dp:
        #     return dp[i]
        if i >= len(s):
            return 1
        
        if s[i] == "0":
            return 0
        
        res = dfs(i+1)

        if (i + 1 < len(s) and (s[i] == "1" or
        s[i] == "2" and s[i+1] in "0123456")):
            res += dfs(i+2)

        return res
    return dfs(0)
    
print(numDecodings("121"))