def Merge(dict1,dict2):
    return dict2.update(dict1)
dict1={"a":1,"b":2,"c":3,"d":4}
dict2={"e":5,"f":6,"g":7,"h":8}
print(Merge(dict1,dict2))
print(dict2)