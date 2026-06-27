# program to remove duplicate characters
s=input("enter a string: ")
result=""
for ch in s:
    if ch not in result:  #if the character is not already in result,add it.
        result=result+ch
print("string after removing duplicate characters: ",result)        