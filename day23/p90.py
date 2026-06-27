# To find first repeating character in a string
s=input("Enter a string: ")
for ch in s:
    if s.count(ch)>1:
        print("First repeating character :",ch)
        print(s.count(ch))
        break
else:
    print("No repeating character found")