
"""
Failed miserably in this approach
"""
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)

    for l in range(len(temperatures)-1):
        r = l + 1
        count = 0
        if temperatures[l] < temperatures[r]:
            count += 1
            res[l] = count
        else:
            while r < len(temperatures)-1 and temperatures[l] > temperatures[r]:
                print(l, r)
                count += 1
                r += 1
            
            res[l] = count 
            # print (res)
    return res


def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([t, i])
    return res



temperatures = [73,74,75,71,69,72,76,73] # Expected : [1,1,4,2,1,1,0,0], mine: [1, 1, 4, 2, 1, 1, 1]
# temperatures = [30,40,50,60] # Expected : [1,1,1,0], mine: [1, 1, 1]
# temperatures =[30,60,90]
# print(dailyTemperaturesfailed(temperatures))  #Failed approach
print(dailyTemperatures(temperatures))

