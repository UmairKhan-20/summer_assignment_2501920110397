# program to check palindrome string
s=input("Enter a string: ")
if s==s[::-1]:
    print("String is Palindrome")
else:
    print("String is not Palindrome")