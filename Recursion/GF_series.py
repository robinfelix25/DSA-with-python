
#TODO: Need to figure out is it possible to print out all output of recursion?

def gfseries(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    trend = gfseries(n-2)**2 - gfseries(n-1)
    print (trend, end= ' ')
    return trend

# print(gfseries(6))
# gfseries(3)
gfseries(6)