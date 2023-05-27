

def howsum(targetsum, numbers, memo = {}):
    if targetsum in memo: return memo[targetsum]
    if targetsum == 0: return []
    if targetsum < 0: return None

    for n in numbers:
        reminder = targetsum - n
        reminderResult = howsum(reminder, numbers, memo)

        if reminderResult != None:
            reminderResult = reminderResult + [n]
            memo[targetsum] = reminderResult
            return reminderResult
        
    memo[targetsum] = None
    return None

numbers = [5,3,4,7]
targetsum = 7
print(howsum(targetsum, numbers))
print(howsum(300, [7,14]))