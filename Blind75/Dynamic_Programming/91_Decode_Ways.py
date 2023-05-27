
# def numDecodings(s):
    # res = []

    # def dfs(idx, cur):
    #     # if cur != '' or  
    #     res.append(cur[:])

    #     for i in range(idx, len(s)):
    #         dfs(i+1, cur + s[i])

    # dfs(0, '')
    # return res


def numDecodings(s):
    dp = {len(s) : 1}
    print (dp)

print(numDecodings("226"))