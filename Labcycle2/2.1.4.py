string=input("Enter a string:")
list1=list(string)
list1=[ord(character)+1 for character in list1]
print(list1)