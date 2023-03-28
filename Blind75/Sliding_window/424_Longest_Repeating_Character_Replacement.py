
#TODO Need to come for this problem again revisit

def characterReplacement(s, k):
    count = {}
    l = 0
    res = 0
    def maxcount(count):
        max_c = 0
        for k, v in count.items():
            max_c = max(max_c, v)
        return max_c

    for r in range(len(s)):
        # print (count)
        count[s[r]] = 1 + count.get(s[r], 0)
        print(maxcount(count))
        if (r - l + 1) - maxcount(count) <= k:
            res = max((r-l+1), res)
        else:
            count[s[l]] -= 1
            l += 1

    return res

s = "ABAB"
k = 2
print(characterReplacement(s,k))

