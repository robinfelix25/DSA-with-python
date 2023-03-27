
def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        cursum = numbers[l] + numbers[r]
        if cursum > target:
            r -= 1
        elif cursum < target:
            l += 1
        else:
            return [l+1, r+1]

numbers = [2,7,11,15]
target = 9 
print(twoSum(numbers, target))