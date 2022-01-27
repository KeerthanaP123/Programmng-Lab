n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n1>n2:
    smaller=n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if(n1%i==0)and(n2%i==0):
        gcd=i
print("GCD of",n1,"and",n2,"is",gcd)