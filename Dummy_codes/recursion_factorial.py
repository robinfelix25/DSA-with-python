

def factorial_rec(n):
    if n == 1:
        return 1
    else:
        fact = factorial_rec(n - 1)
        return fact * n
    
print(factorial_rec(4))

#fact in itertative way

def factorial_itr(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n -= 1

    return fact

print (factorial_itr(4))