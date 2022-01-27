str=input("Enter a string")
word=input("Enter  to count")
a=[]
count=0
a=str.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count=count+1
print("Count of word is",count)