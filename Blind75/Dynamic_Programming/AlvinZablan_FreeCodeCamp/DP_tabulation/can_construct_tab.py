
def canconstruct_sol1(target, words):
    dp = [False for _ in range(len(target)+1)]
    dp[0] = True

    for i in range(len(target)+1):
        if dp[i] == True:
            for word in words:
                if target[i: i+len(word)] ==  word:
                    dp[i+len(word)] = True

    print(dp)
    return dp[len(target)]

print(canconstruct_sol1('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct_sol1('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['ee','eee','eeee','eeeee','eeeeeee']))