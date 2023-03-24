
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2},
}

def nestedEvenSum(obj, sum=0):
    # TODO
    for v in obj:
        if type(obj[v]) == dict:
            sum += nestedEvenSum(obj[v])
        elif type(obj[v]) == int and obj[v]%2 == 0:
            sum += obj[v]
    return sum

print (nestedEvenSum(obj2))

