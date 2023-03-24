

"""
This Seems like a good question to understand how to have
a temp variable or list and return that value to the output in recursion
"""
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return []
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']