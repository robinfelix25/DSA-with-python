
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    element = arr.pop()
    return element * productOfArray(arr)


print (productOfArray([1,2,3])) #6
print (productOfArray([1,2,3,10])) #60