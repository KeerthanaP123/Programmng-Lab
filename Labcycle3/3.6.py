lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))
list=[x for x in range(lower,upper+1) if x**.5==int(x**.5)]
list=[x for x in list if x%2==0]
print(list)