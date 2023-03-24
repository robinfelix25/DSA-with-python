# Created By : Robin Felix (buildwithfelix@gmail.com)

def dectobinary(decimal):
    assert type(decimal) == int, "Decimal number should be binary"
    if decimal == 0:
        return str(decimal)
    reminder = decimal % 2
    quotient = decimal // 2
    reminder = str(reminder) + dectobinary(quotient)
    return reminder

print(dectobinary(10))