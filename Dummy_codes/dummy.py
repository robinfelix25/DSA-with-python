

def dummy(numbers, target):
    hashmap = {}
    res = []
    for i, n in enumerate(numbers):
        diff = target - n
        if diff in hashmap:
            res.append(i)

    return res


numbers = [2,7,11,15]
target = 9
# Output: [1,2]
print(dummy(numbers, target))
        
        






