# Created By: Robin Felix(buildwithfelix@gmail.com)

# In Python we have pow() inbuilt function to do that, Just Curious to Implement it and try
# Estimated the excution time of both the inbuit and custom made function to using timeit module
# Noticed there is not big difference
import timeit

def power(x, n):
    """
    Args:
    x - Base number
    n - exponent
    """
    assert type(n) == int, "Exponent (n) must be integer"
    if n <= 0:
        return 1
    return x * power(x, n-1 )

# TEST CASE : 1
# print(power(-3,2))

# TEST CASE : 2
# print(power(-3,2.5))

# TEST CASE : 3
# print(power(4,-1)) # Need to understand the math behind it