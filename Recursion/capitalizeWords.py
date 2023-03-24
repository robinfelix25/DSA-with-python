
def capitalizeWords(arr):
    # TODO
    result = []
    if len(arr) == 0:
        return arr
    result.append(arr[0].upper())
    result += capitalizeWords(arr[1:])
    return result


arr = ['i', 'am', 'learning', 'recursion']

print(capitalizeWords(arr))