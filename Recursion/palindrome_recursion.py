

def ispalindrome(word):
    if len(word) == 0:
        return True
    if word[0] != word[-1]: 
        return False
    return ispalindrome(word[1:-1])


print(ispalindrome("mad"))