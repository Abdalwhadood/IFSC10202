

class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores   # list of strings

    def RunningAverage(self):
        total = 0
        count = 0

        for grade in self.Grades:
            if grade != "":   # ignore blanks
                total += float(grade)
                count += 1

        if count == 0:
            return 0
        return total / count

    def TotalAverage(self):
        total = 0
        count = len(self.Grades)

        for grade in self.Grades:
            if grade == "":
                total += 0
            else:
                total += float(grade)

        if count == 0:
            return 0
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



print(f"{'First':>12} {'Last':>12} {'ID':>12} {'Running':>12} {'Semester':>12} {'Letter':>12}")
print(f"{'Name':>12} {'Name':>12} {'Number':>12} {'Average':>12} {'Average':>12} {'Grade':>12}")
print("-" * 72)


file = open("10.Project Student Scores.txt", "r")


for line in file:
    line = line.strip()
    parts = line.split(",")

    firstname = parts[0]
    lastname = parts[1]
    tnumber = parts[2]

    scores = parts[3:]   # rest are scores

    # create student object
    student = Student(firstname, lastname, tnumber, scores)

    # get values
    run_avg = student.RunningAverage()
    sem_avg = student.TotalAverage()
    letter = student.LetterGrade()

    # print formatted output
    print(f"{firstname:>12} {lastname:>12} {tnumber:>12} {run_avg:12.2f} {sem_avg:12.2f} {letter:>12}")

file.close()