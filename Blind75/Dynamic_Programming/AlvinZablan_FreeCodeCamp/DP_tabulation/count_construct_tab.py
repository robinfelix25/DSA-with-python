

def count_construct_memo(target, words, memo = {}):
    if target in memo: return memo[target]
    if target == '': return 1
    
    count = 0
    for word in words:
        if target.startswith(word):
            noofways = count_construct_memo(target[len(word):], words, memo)
            count += noofways

    memo[target] = count
    return count


# print(count_construct_memo('purple',['purp','p','ur','le','purpl']))

def count_construct_tab(target, words):
    dp = [0 for _ in range(len(target)+1)]
    dp[0] = 1

    for i in range(len(target)+1):
        for word in words:
            if target[i:i+len(word)] == word:
                dp[i+len(word)] += dp[i]
    
    print(dp)
    return dp[len(target)]

print(count_construct_tab('purple',['purp','p','ur','le','purpl']))