list=[]
num=int(input("Enter the limit:"))
for i in range(num):
    number=int(input("Enter the values:"))
    list.append(number)
print("Sum of items in the list",sum(list))