

def reverse(strng):
    if len(strng) == 0:
        return ''
    return reverse(strng[1:]) + strng[0] 

strng = "python"
print(reverse(strng))