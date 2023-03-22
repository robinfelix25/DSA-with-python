

def factorial_rec(n):
    assert n >= 0 and type(n) == int, 'number must be +ve integer only'
    if n == 1:
        return 1
    else:
        fact = factorial_rec(n - 1)
        return fact * n
    
print(factorial_rec(5))

#fact in itertative way

def factorial_itr(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n -= 1

    return fact

print (factorial_itr(4))