

#TODO Need to come for this problem again revisit

# tuto code
def lengthOfLongestSubstring(s):
    l = 0
    charset = set()
    res = 0
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l += 1
        charset.add(s[r])
        res = max(res, r - l + 1)
    return res

s= "pww"
print(lengthOfLongestSubstring(s))

def lengthOfLongestSubstring_mysol(s):
    window = set()
    l, r =0, 0
    max_l = 0

    while r < len(s):
        if s[r] not in window:
            window.add(s[r])
            r += 1
        else:
            window.remove(s[l])
            l += 1
        max_l = max(max_l, r - l )

    return max_l

s= "pww"
print(lengthOfLongestSubstring_mysol(s))
