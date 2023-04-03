

def evalRPN(tokens):
    stack = []

    for t in tokens:
        if t == "+":
            stack.append(stack.pop() + stack.pop())
        elif t == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif t == '*':
            stack.append(stack.pop() * stack.pop())
        elif t == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b)/a)) #this line is getting diff with python version some work with 
            stack.append(int(b/a)) #this line also
        else:
            stack.append(int(t))
    return stack[0]


# tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))
