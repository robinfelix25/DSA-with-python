# Created By : Robin Felix (buildwithfelix@gmail.com)


#Iterative approcah
def fibonacci_itr(n):
    assert n>=0 and type(n) == int, "Fibonacci number should be +ve integer"
    first = 0
    second = 1
    for i in range(n):
        print(first)
        third = first + second
        first = second
        second = third
        
# fibonacci_itr(5)

# Recursive approach

def fibnocci_recur(n):
    assert n>=0 and type(n) == int, "Fibonacci number should be +ve integer"
    if n in [0, 1]:
        return n
    else:
        # trend = fibnocci_recur(n-2) + fibnocci_recur(n-1)
        first = fibnocci_recur(n-2)
        second = fibnocci_recur(n-1)
        print(first, second)
        trend = first + second
        print(trend, end = " ")
        return trend
    
# print(fibnocci_recur(4))
fibnocci_recur(4)
