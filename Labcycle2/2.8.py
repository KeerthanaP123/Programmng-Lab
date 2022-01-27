str1=input("Enter first string:")
str2=input("Enter second string:")
print(str1.replace(str1[0],str2[0]+' '+str2.replace(str2[0],str1[0])))