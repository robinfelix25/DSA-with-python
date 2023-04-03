

def min_distance(v):
    v.sort()
    min_d = float("inf")
    res = []
    # print(v)
    min_dis = float("inf")
    # for i in range(len(v)-1):
    #     diff = abs(v[i] - v[i -1])
    #     min_dis = min(min_dis, diff)
    # print(min_dis)

    # for i in range(len(v)-1):
    #     if abs(v[i] - v[i -1]) == min_dis:
    #         res.append((v[i -1],v[i]))
    # return min_dis, res
    for i in range(len(v)-1):
        res = []
        diff = abs(v[i] - v[i -1])
        min_dis = min(min_dis, diff)
        if diff == min_dis:
            res.append((v[i - 1], v[i]))
        # else:
        #     res = []
    return min_dis, res 



v =[3,12,126,44,52,57,144,61,68,72,122]
print(min_distance(v))