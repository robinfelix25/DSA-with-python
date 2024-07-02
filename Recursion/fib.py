# def fib(n):
#     first = 0
#     second = 1

#     for i in range(n):
#         third = first + second
#         first = second
#         second = third
#         print(third)

# fib(5)


# def fib_memo(n):
#     if n <= 2: return 1
#     res = fib_memo(n-1) + fib_memo(n-2)
#     return res

# print(fib_memo(50))


def fib_memo(n, memo= {}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    res = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = res
    return res

print(fib_memo(50))