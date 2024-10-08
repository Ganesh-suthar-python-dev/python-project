student = { }#that is empty dist

def add_student(name , marks):
    student[name] = marks
    print(f"the student {name} and the student marks {marks} are added ")

def view_student():
    if student :
        for name , marks in student.items():
            print(f"{name }:{marks}")
    else :
        print("not student at the time ")

def delete_student(name):
    if name in student:
        del student[name]
        print(f"the student {name} are deleted ")
    else :
        print(f"the student {name} not founded")

def update_studnet(name,marks):
    if name in student:
        student[name] = marks
        print(f"the student {name} and the marks {marks} are updated ")
    else:
        print(f"the student {name} not found ")

    
while True:
        print("'1 add the student ")
        print("'2 view the student list")
        print("'3 delete the student ")
        print("'4 update the student")
        print("'5 exit")

        choice = int(input("Enter your choice (1-5) : "))

        if choice ==1:
            name = input("Enter the student name ")
            marks = float(input("Enter the student marks : "))
            add_student(name,marks)
        elif choice ==2:
            view_student()
        elif choice ==3:
            name = input("Enter the student name : ")
            delete_student(name)
        elif choice ==4:
            name = input("Enter the student : ")
            marks = float(input("Enter the student marks : "))
            update_studnet(name , marks)
        elif choice ==5:
            print("Thnaks for useing my student system ❤ ")
            print("we are exit in the system")
        else :
            print("the invalid choice plz try again")
    
            