

def longestConsecutive(nums):
    numset = set(nums)
    longest = 0

    for n in nums:
        if n-1 not in numset:
            length = 1
            while n+length in numset:
                length += 1
            longest = max(longest, length)
    return longest

    # nums = set(nums)
    # longest = 0
    # for n in nums:
    #     if n - 1 not in nums:
    #         length = 0
    #         temp = n
    #         for _ in range(len(nums)):
    #             if temp in nums:
    #                 temp = temp + 1
    #                 length += 1
    #             else:
    #                 break
    #         longest = max(length, longest)
    # return longest

nums = [100, 2, 200, 1,3, 4]

print(longestConsecutive(nums))