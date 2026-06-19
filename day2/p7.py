# product of digits
num=int(input("Enter the number: "))
product=1
while num>0:
    digit=num%10
    product*=digit
    num=num//10
print("Product of digits= ",product)    