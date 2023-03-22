#Iterative approcah

def fibonacci_itr(n):
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
    if n in [0, 1]:
        return n
    else:
        return fibnocci_recur(n-2) + fibnocci_recur(n-1)
    
print(fibnocci_recur(4))
