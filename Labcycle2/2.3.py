li=int(input("Enter the number of names:"))
count=0
for i in range(li):
    a=str(input("Enter the names:"))
    count+=a.count('a')
    count+=a.count('A')
print(count)