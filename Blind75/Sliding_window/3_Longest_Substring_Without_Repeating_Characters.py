

#TODO Need to come for this problem again revisit

def lengthOfLongestSubstring(s):
    l = 0
    charset = set()
    res = 0
    for r in range(len(s)):
        while s[r] in charset:
            print(s[l])
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r - l + 1)
    return res

s= "pww"
print(lengthOfLongestSubstring(s))
