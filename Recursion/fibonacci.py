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
        # res1 = fibnocci_recur(n-2) 
        # res2 = fibnocci_recur(n-1)
        # res = res1 + res2
        # return res
        return fibnocci_recur(n-1) + fibnocci_recur(n-2)  
    
# print(fibnocci_recur(3))


