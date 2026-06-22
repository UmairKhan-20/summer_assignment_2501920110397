rows=int(input("enter the number of rows: "))
cols=int(input("enter the number of columns: "))
for i in range(rows):
    sum=0
    for j in range(cols):
        num=int(input("enter the elements: "))
        sum=sum+num
    print("sum of row", sum)