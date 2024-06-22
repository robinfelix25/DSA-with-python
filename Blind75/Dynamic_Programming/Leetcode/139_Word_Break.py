'''
Implemented the recursive approach with memo
'''
#working solution in recursion with memo
def wordBreak_sol1(s, worddict):
    def dfs(s, memo = {}):
        if s in memo: return memo[s]
        if len(s) == 0:
            return True
        
        for w in worddict:
            if s.startswith(w):
                if dfs(s[len(w):], memo):
                    memo[s] = True
                    return True
        memo[s] = False
        return False
    
    return dfs(s)

print(wordBreak_sol1('leetcode', ['leet', 'code']))

# Above recursive DP solution is implemented in Tabulation (bottom up)
def wordBreak_tab(s, worddict):
    dp = [False ] * (len(s)+1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in worddict:
            if ( i +len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]

print(wordBreak_tab('leetcode', ['leet', 'code']))
# def wordBreak_rec(s, worddict, memo = {}):
#     print(memo)
#     if s in memo: return memo[s]
#     if len(s) == 0:
#         return True
    
#     for w in worddict:
#         if s.startswith(w):
#             if wordBreak_rec(s[len(w):], worddict, memo):
#                 memo[s] = True
#                 return True
#     memo[s] = False
#     return False
# print(wordBreak_rec('leetcode', ['leet', 'code']))
# print(wordBreak_rec("a",["b"]))
