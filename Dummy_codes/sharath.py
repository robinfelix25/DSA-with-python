# print("hello world")


# from collections import Counter

# def count_numbers(input_list):
#     # Use Counter to count occurrences of each number
#     counts = Counter(input_list)

#     # Create a list of tuples with number and its count
#     result = [(number, count) for number, count in counts.items()]

#     return result

# Example usage:
# nums = [5,5,5,7,7,3,4,7]
# # input_list = [1, 2, 3, 1, 2, 1, 4, 5, 4, 3, 5, 5]
# result = count_numbers(nums)
# print(result)

# def counter(nums):
#     counts = {}
#     for item in nums:
#         counts[item] = counts.get(item, 0) + 1
#     return counts

# # def pack(nums):
# #     hash = set()
# #     result = []
# #     for n in nums:
# #         if n in hash:
# #             count = 




# nums = [5,5,5,7,7,3,4,7]
# # print(pack(nums))
# print(counter(nums))

def packNumbers(nums):
    if not nums:
        return []

    result = []
    cur_no = nums[0]
    cur_count = 1

    for i in range(1, len(nums)):
        if nums[i] == cur_no:
            cur_count += 1
        else:
            if cur_count == 1:
                result.append(cur_no)
                cur_no = nums[i]
                cur_count = 1
                continue
            result.append(f"{cur_no}:{cur_count}")
            cur_no = nums[i]
            cur_count = 1

    if cur_count != 1: 
        result.append(f"{cur_no}:{cur_count}")
    else:
        result.append(cur_no)

    return result


nums = [5,5,5,7,7,3,4,7, 5]
result = packNumbers(nums)
print(result)





# nums = [5,5,5,7,7,3,4,7]
# result = packNumbers2(nums)
# print(result)