# Write a program to find all pairs of integers whose sum is equal to a given number

input = [2,6,3,9,11]
target = 9

for num in input:
    diff = target - num
    if diff in input:
        print (num, diff)



