
# Student Record Management System using Singly Linked List

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # Add Student
    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully!")

    # Display Students
    def display(self):
        if self.head is None:
            print("No student records found!")
            return

        print("\nRoll No\tName\tMarks")
        temp = self.head

        while temp:
            print(temp.roll, "\t", temp.name, "\t", temp.marks)
            temp = temp.next

    # Delete Student
    def delete(self, roll):
        temp = self.head
        prev = None

        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Student deleted successfully!")
                return

            prev = temp
            temp = temp.next

        print("Student not found!")

    # Update Student
    def update(self, roll, name, marks):
        temp = self.head

        while temp:
            if temp.roll == roll:
                temp.name = name
                temp.marks = marks
                print("Student updated successfully!")
                return

            temp = temp.next

        print("Student not found!")

    # Search Student
    def search(self, roll):
        temp = self.head

        while temp:
            if temp.roll == roll:
                print("Student Found!")
                print("Roll No:", temp.roll)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student not found!")

    # Sort Students
    def sort(self, key, order):
        students = []
        temp = self.head

        while temp:
            students.append(temp)
            temp = temp.next

        if key == "marks":
            students.sort(key=lambda x: x.marks,
                          reverse=(order == "desc"))
        else:
            students.sort(key=lambda x: x.roll,
                          reverse=(order == "desc"))

        # Rebuild linked list in sorted order
        self.head = None

        for student in students:
            student.next = None

            if self.head is None:
                self.head = student
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = student

        print("Records sorted successfully!")


# Main Program
s = StudentList()

while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Sort Records")
    print("6. Display Records")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        s.add(roll, name, marks)

    elif choice == 2:
        roll = int(input("Enter Roll Number to delete: "))
        s.delete(roll)

    elif choice == 3:
        roll = int(input("Enter Roll Number to update: "))
        name = input("Enter New Name: ")
        marks = float(input("Enter New Marks: "))
        s.update(roll, name, marks)

    elif choice == 4:
        roll = int(input("Enter Roll Number to search: "))
        s.search(roll)

    elif choice == 5:
        key = input("Sort by (marks/roll): ").lower()
        order = input("Order (asc/desc): ").lower()

        if key in ("marks", "roll") and order in ("asc", "desc"):
            s.sort(key, order)
        else:
            print("Invalid sorting option!")

    elif choice == 6:
        s.display()

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
