# Created By : Robin Felix (buildwithfelix@gmail.com)

def sumofdigits(n):
    """
    Args:
    n : Number that sum need to be returned
    """
    assert n>=0 and type(n) == int, "n should be +ve integer"
    if n == 0:
        return 0
    digit = n//10
    reminder = n%10
    return  reminder + sumofdigits(digit)

# print (sumofdigits(-4))
print (sumofdigits(4))