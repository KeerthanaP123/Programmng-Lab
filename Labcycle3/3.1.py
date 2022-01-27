num=int(input("Enter the number:"))
factorial=1
if(num<0):
    print("factorial of negative number does not exists")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    for i in  range(1,num+1):
        factorial=factorial*i
    print("Factorial of",num,"is",factorial)