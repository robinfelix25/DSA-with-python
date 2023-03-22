# Created By : Robin Felix (buildwithfelix@gmail.com)

# Solution 1

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    countS, countT = {}, {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    return countS == countT

s = "anagram"
t = "nagaram"

# s = "rat"
# t = "cat"
print (isAnagram(s, t))

# Solution 2
s = "robin"
t = "niobr"

def isAnagramTwo(s, t):
    freq = [0] * 26

    if len(s) !=  len(t):
        return False
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1

    for n in freq:
        if n != 0:
            return False
    
    return True

print (isAnagramTwo(s, t))