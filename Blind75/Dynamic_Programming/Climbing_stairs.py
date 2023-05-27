
# back tracking brute force, still can be improved
count = 0
def stairs(n):
    def dfs(res):
        global count
        # print(res)
        if res == n:
            count +=1
            return
        if res > n:
            return
        
        for i in [1,2]:
            dfs(res + i)
    dfs(0)
    return count
n = 200
print(stairs(n))