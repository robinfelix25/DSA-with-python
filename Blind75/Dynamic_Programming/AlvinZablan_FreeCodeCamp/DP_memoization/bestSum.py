

def bestsum(target, nums, memo = {}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortcombination = None
    for n in nums:
        reminder = target - n
        reminderres = bestsum(reminder, nums, memo)

        if reminderres != None:
            remindercomb = reminderres + [n]
            if shortcombination == None or len(remindercomb) < len(shortcombination):
                shortcombination = remindercomb 

    memo[target] = shortcombination
    return shortcombination























#     if target == 0: return []
#     if target < 0: return None

#     shortcombination = None
#     for n in nums:
#         reminder = target - n
#         remindercomb = bestsum(reminder, nums)

#         if remindercomb != None:
#             combination = remindercomb + [n] 
#             if shortcombination == None or len(combination) < len(shortcombination):
#                 shortcombination = combination
#     return shortcombination


print(bestsum(7, [5,3,4,7]))
print(bestsum(100, [1,2,5,25]))