

'''
THis code is bit tough to understand Lets try another approach
'''
def isValid1(s):
    map = {')':'(', '}' : '{', ']' : '['}
    stack = []

    for i in s:
        if i not in map:
            stack.append(i)
            print (stack)
            continue
        if not stack or stack[-1] != map[i]:
            return False
        stack.pop()

    print(stack)
    return not stack

# s = '()[]{}'
# print(isValid(s))

'''
If Feel this code is pretty easy to understand
'''
def isValid2(s):
    map = {')':'(', '}' : '{', ']' : '['}
    stack = []

    for c in s:
        if c in map:
            if stack and stack[-1] == map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

s = '()[]{}'
print(isValid2(s))