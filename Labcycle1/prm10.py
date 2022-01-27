string=input("Enter a string")
newstring=string[-1:] + string[1:-1] + string[:1]
print(newstring)