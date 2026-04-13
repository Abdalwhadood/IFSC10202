
class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []  

    
    def RunningAverage(self):
        total = 0
        count = 0

        for grade in self.Grades:
            if grade != "":
                total += float(grade)
                count += 1

        if count == 0:
            return 0
        return total / count

    
    def TotalAverage(self):
        total = 0
        count = len(self.Grades)

        if count == 0:
            return 0

        for grade in self.Grades:
            if grade == "":
                total += 0
            else:
                total += float(grade)

        return total / count

    
    def LetterGrade(self):
        avg = self.TotalAverage()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"



class StudentList:
    def __init__(self):
        self.Studentlist = []

    
    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    
    def find_student(self, tnumber):
        for i in range(len(self.Studentlist)):
            if self.Studentlist[i].TNumber == tnumber:
                return i
        return -1

    
    def print_student_list(self):
        print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
        print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
        print("-" * 72)

        for student in self.Studentlist:
            run_avg = student.RunningAverage()
            sem_avg = student.TotalAverage()
            letter = student.LetterGrade()

            print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
                  f"{run_avg:12.2f} {sem_avg:12.2f} {letter:>12}")

    
    def add_student_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                self.add_student(firstname, lastname, tnumber)

    
    def add_scores_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                tnumber = parts[0]
                score = parts[1] if len(parts) > 1 else ""

                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(score)



def main():
    students = StudentList()

    
    students.add_student_from_file("11.Project Students.txt")
    students.add_scores_from_file("11.Project Scores.txt")

    
    students.print_student_list()



main()