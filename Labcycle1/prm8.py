list=[1,2,3,4,5,6,7,8,9,10]
for even in list:
    if even%2==0:
        list.remove(even)
print("List withoue even number are",list)