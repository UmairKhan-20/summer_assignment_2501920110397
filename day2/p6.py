# reverse number program
num=int(input("enter a number: "))
reversed=0
while num>0:
    rem=num%10
    reversed=(reversed*10)+rem
    num=num//10
    
print("Reverse of the number is:",reversed)    

    

    