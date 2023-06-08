                
def allconstruct_sol1(target, words):
    res = []
    def dfs(cur, temp):
        if cur == target:
            res.append(temp)
            return True
        if len(cur) > len(target):
            return False
        
        for w in words:
            dfs(cur+w, temp + [w])

    dfs('',[])
    return res

print(allconstruct_sol1('purple',['purp','p','ur','le','purpl']))

def allconstruct_memo(target, words):
    res = []
    def dfs(cur, temp, memo = {}):
        if cur in memo: return memo[cur]
        if cur == target:
            res.append(temp)
            return True
        if len(cur) > len(target):
            return False
        
        for w in words:
            ret = dfs(cur+w, temp + [w], memo)
            memo[cur + w] = ret
        # print(memo)
    dfs('',[])
    return res
print(allconstruct_memo('purple',['purp','p','ur','le','purpl']))

def allconstruct(target, words):
    if target == '': return [[]]
    
    res = []
    for word in words:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixways = allconstruct(suffix, words)
            print(suffixways)
            targetways = suffixways + [word] 
            print(targetways)
            res.append(targetways)
    return res
# print(allconstruct_sol1('purple',['purp','p','ur','le','purpl']))
# print(allconstruct('purple',['purp','p','ur','le','purpl']))