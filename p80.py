# program to find column-wise sum
rows=int(input("enter the number of rows: "))
cols=int(input("enter the number of columns: "))
for j in range(cols):
    sum=0
    for i in range(rows):
        num=int(input("enter the elements: "))
        sum=sum+num
    print("sum of column", sum)