list=[]
limit=int(input("Enter limit:"))
for i in range(limit):
    a=int(input("Enter values:"))
    list.append("Over" if a>100 else a)
print(list)