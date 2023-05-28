
'''
Explored Three different types of solution

Solution 1:
- For loop takes care of the append & pop of cur list, when loop exists the values are lost
- easy to implement template

Solution 2:
- Almost the same as first solution
- we are taking of the push and pop operation, i will its not mandatory

Solution 3:
- multi recursion to avoid the for loop
- Need to find out the advantages in it ... for vs multi_recursion
- Can keep it as another technique
'''
def subsets_sol1(nums):
    res = []

    def dfs(index, path):
        res.append(path.copy())
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return res

def subsets_sol2(nums):
    res = []

    def dfs(index, path):
        res.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return res

def subsets_sol3(nums):
    res = []
    curr = []

    def dfs(i):
        if i >= len(nums):
            res.append(curr[:])
            return
        
        #include i
        curr.append(nums[i])
        dfs(i + 1)

        #not include i
        curr.pop()
        dfs(i + 1)

    dfs(0)
    return res
        
nums = [1,2,3]
print(subsets_sol1(nums))
print(subsets_sol2(nums))
print(subsets_sol3(nums))