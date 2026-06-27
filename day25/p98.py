# program to find common characters in string
s1=input("enter string1: ")
s2=input("enter string2: ")
print("common characters are: ")
for ch in s1:
    if ch in s2:
        print(ch,end=" ")