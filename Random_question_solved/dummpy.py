def longest_consecutive_sequence(list):
    count = 0
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            count += 1
        else:
            count = 1
    return count
list = ["a", "b", "c", "c", "c", "e"]
print(longest_consecutive_sequence(list))