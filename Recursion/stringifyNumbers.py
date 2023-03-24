obj1 = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

def stringifyNumbers(obj):
    # TODO
    for k in obj:
        if type(obj[k]) == int:
            obj[k] = str(obj[k])
        elif type(obj[k]) == dict:
            stringifyNumbers(obj[k])
    return obj


print(stringifyNumbers(obj1))