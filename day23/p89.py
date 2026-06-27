# To find first non repeating character in a string
s=input("Enter a string: ")
for ch in s:
    if s.count(ch)==1:
        print("First non repeating character :",ch)
        break
else:
    print("No non repeating character found")
        
        