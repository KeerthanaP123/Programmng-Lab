list=["Hello","World","programming","python","data structure","maths"]
print(list)
a=0
for i in list:
    a=len(i)if len(i)>a else a
print(a)