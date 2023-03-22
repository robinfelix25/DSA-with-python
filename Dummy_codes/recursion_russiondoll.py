# Created By : Robin Felix (buildwithfelix@gmail.com)

# def russiandoll(doll):
#     if doll == 1:
#         print("all dolls are opened")
#     else:
#         russiandoll(doll-1)
#         print(f"Doll {doll} is opened")

# russiandoll(10)

# print("*"*20)
# def russiandolliter(doll):
#     print("all dolls are opened")
#     while doll > 0:
#         print(f"Doll {doll} is opened")
#         doll -= 1
    

# russiandolliter(10)

def poweroftwo(n):
    power = 1
    i = 0
    while i < n:
        power = power * 2
        i = i + 1
    print (power)

# poweroftwo(3)

def poweroftworec(n):
    if n == 0:
        return 1
    else:
        power = poweroftworec(n - 1)
        return power * 2
print (poweroftworec(3))

print(pow(2,3))