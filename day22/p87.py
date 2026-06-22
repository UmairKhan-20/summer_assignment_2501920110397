# counting characters in a string
s=input("Enter a String: ")
ch=input("Enter the character: ")
count=0
for i in s:
    if i==ch:
        count+=1
print("Number of occurrences of character is: ",count)