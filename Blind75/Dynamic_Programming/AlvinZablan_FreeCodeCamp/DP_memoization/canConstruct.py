

# My solution
def canconstruct_sol1(target, words):
    
    def dfs(cur):
        if cur == target:
            return True
        if len(cur) > len(target):
            return False
        
        for w in words:
            if dfs(cur+w):
                return True
            
        return False
    
    return dfs('')

# tuto solution
def canconstruct(target, words, memo= {}):
    if target in memo: return memo[target]
    if target == '': return True

    for word in words:
        if target.startswith(word):
            suffix = target[len(word):]
            if canconstruct(suffix, words, memo):
                memo[target] = True
                return True
    memo[target] = False
    # print(memo)
    return False
        

print(canconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['ee','eee','eeee','eeeee','eeeeeee']))