
class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):
        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code



class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []


    def ReadEmployeeFile(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    data = [x.strip() for x in data]

                    emp = Employee(
                        int(data[0]), data[1], data[2],
                        data[3], data[4], data[5], data[6]
                    )
                    self.employees.append(emp)
        except FileNotFoundError:
            print("File not found. Starting with empty list.")


    def WriteEmployeeFile(self):
        with open(self.filename, "w") as file:
            for e in self.employees:
                line = f"{e.emp_num}, {e.first}, {e.last}, {e.address}, {e.city}, {e.state}, {e.zip_code}\n"
                file.write(line)
        print("File saved.")


    def DisplayEmployeeList(self):
        print("\nEmployee        First           Last            Address         City            State           Zip")
        print("Number          Name            Name")
        print("-" * 95)

        for e in self.employees:
            print(f"{e.emp_num:<15}{e.first:<15}{e.last:<15}{e.address:<15}{e.city:<15}{e.state:<15}{e.zip_code:<15}")


    def FindEmployee(self, emp_num):
        for i, e in enumerate(self.employees):
            if e.emp_num == emp_num:
                return i
        return -1


    def NextEmployeeNumber(self):
        if not self.employees:
            return 1
        return self.employees[-1].emp_num + 1

    def AddEmployee(self, first, last, address, city, state, zip_code):
        emp_num = self.NextEmployeeNumber()
        new_emp = Employee(emp_num, first, last, address, city, state, zip_code)
        self.employees.append(new_emp)
        print("Employee Added")


    def DeleteEmployee(self, emp_num):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Employee not found.")
        else:
            del self.employees[index]
            print("Employee Deleted")


    def UpdateEmployee(self, emp_num, field, value):
        index = self.FindEmployee(emp_num)
        if index == -1:
            print("Employee not found.")
            return

        emp = self.employees[index]

        if field == "F":
            emp.first = value
        elif field == "L":
            emp.last = value
        elif field == "A":
            emp.address = value
        elif field == "C":
            emp.city = value
        elif field == "S":
            emp.state = value
        elif field == "Z":
            emp.zip_code = value



def valid_state(state):
    return len(state) == 2 and state.isupper()


def valid_zip(zip_code):
    return zip_code.isdigit() and len(zip_code) == 5


def required_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required.")



def main():
    emp_list = EmployeeList("Final Project Employees.txt")
    emp_list.ReadEmployeeFile()

    while True:
        print("\n(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")

        choice = input("\nEnter Selection: ").upper()

        if choice == "A":
            first = required_input("Enter First Name: ")
            last = required_input("Enter Last Name: ")
            address = required_input("Enter Address: ")
            city = required_input("Enter City: ")

            while True:
                state = input("Enter State (2 uppercase letters): ")
                if valid_state(state):
                    break
                print("Invalid state.")

            while True:
                zip_code = input("Enter Zip (5 digits): ")
                if valid_zip(zip_code):
                    break
                print("Invalid zip.")

            emp_list.AddEmployee(first, last, address, city, state, zip_code)

        elif choice == "D":
            try:
                num = int(input("Enter Employee Number: "))
                emp_list.DeleteEmployee(num)
            except:
                print("Invalid number.")

        elif choice == "C":
            try:
                num = int(input("Enter Employee Number: "))
            except:
                print("Invalid number.")
                continue

            if emp_list.FindEmployee(num) == -1:
                print("Employee not found.")
                continue

            while True:
                print("\n(F)irst Name")
                print("(L)ast Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack")

                field = input("Enter Selection: ").upper()

                if field == "B":
                    break

                value = input("Enter new value: ")

                if field == "S" and not valid_state(value):
                    print("Invalid state.")
                    continue

                if field == "Z" and not valid_zip(value):
                    print("Invalid zip.")
                    continue

                emp_list.UpdateEmployee(num, field, value)

        elif choice == "P":
            emp_list.DisplayEmployeeList()

        elif choice == "S":
            emp_list.WriteEmployeeFile()

        elif choice == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid choice.")



main()