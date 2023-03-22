# Created By : Robin Felix (buildwithfelix@gmail.com)

import collections
def GroupAnagrams(strs):
    ans = collections.defaultdict(list)
    # ans = {}
    print(ans)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    print(ans)
    return ans

strs = ["eat","tea","tan","ate","nat","bat"]
print(GroupAnagrams(strs).values())