
def collectStrings(obj):
    # TODO
    result = []
    for k in obj:
        if type(obj[k]) == str:
            result.append(obj[k])
        elif type(obj[k]) == dict:
            result += collectStrings(obj[k])
            
    return result

obj1 = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
print(collectStrings(obj1))