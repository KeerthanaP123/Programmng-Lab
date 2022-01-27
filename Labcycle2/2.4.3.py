l1=[13,15,78,44,90,345,267,890]
l2=[67,34,321,97,345,13,56,21,567]
list=[]
for i in l1:
    if i in l2:
        list.append(i)
print(list)