# program to develop complete mini project using arrays, strings and functions
# Student Record Management System
roll=[]
name=[]
def add_student():
    r=input("Enter Roll No.: ")
    n=input("Enter Name: ")
    roll.append(r)
    name.append(n)
    print("Student Added")
def view_student():
    if len(roll)==0:
        print("No Records Found")
    else:
        print("Student Records")
        for i in range(len(roll)):
            print("Roll No.:",roll[i],"Name:",name[i])
def delete_student():
    r=input("Enter Roll No. to Delete: ")
    if r in roll:
        i=roll.index(r)
        roll.pop(i)
        name.pop(i)
        print("Record Deleted")
    else:
        print("Student Not Found")
while True:
    print("    Student Record System    ")
    print("1. Add Student")
    print("2.View Student")
    print("3.Delete Student")
    print("4. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add_student()
    elif ch==2:
        view_student()
    elif ch==3:
        delete_student()
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid choice")
