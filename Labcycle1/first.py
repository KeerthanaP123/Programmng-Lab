n1=int(input("Enter start year"))
n2=int(input("Enter final year"))
print("List of leap years")
for year in range(n1,n2):
    if(year%4==0)and(year%100!=0)or(year%400==0):
        print(year)

