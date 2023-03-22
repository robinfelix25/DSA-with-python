# Created By: Robin Felix(buildwithfelix@gmail.com)

# In Python we have pow() inbuilt function to do that, Just Curious to Implement it and try
# Estimated the excution time of both the inbuit and custom made function to using timeit module
# Noticed there is not big difference
import timeit
mycode = '''
def power(x, n):
    """
    Args:
    x - Base number
    n - exponent
    """
    if n == 0:
        return 1
    return x * power(x, n-1 )
power(3,2)
'''

mycode_default = '''
pow(3,2)
'''
print (timeit.timeit(stmt = mycode,
                     number = 10000))

print (timeit.timeit(stmt = mycode_default,
                     number = 10000))
# print(power(3,2))