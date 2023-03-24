# Created By : Robin Felix (buildwithfelix@gmail.com)

def gcd(first, second):
    assert type(first) == int and type(second) == int, "Numbers must be integers"
    if first < 0: #GCD of -ve numbers will also be positive, so changing it to +ve
        first = -1 * first
    if second < 0:
        second = -1 * second

    if second == 0:
        return first
    
    reminder = first%second
    return gcd(second, reminder)

print(gcd(12,8))