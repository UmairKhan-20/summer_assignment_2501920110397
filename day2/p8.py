# palindrome program
num=int(input("Enter a number: "))
temp=num
reversed=0
while num>0:
    digit=num%10
    reversed=(reversed*10)+digit
    num=num//10
if temp==reversed:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
