str=input("Enter string:")
new=str[0]+str[1:].replace(str[0],'$')
print(new)