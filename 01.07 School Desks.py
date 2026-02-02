
a = int(input("Students in Classroom A: "))
b = int(input("Students in Classroom B: "))
c = int(input("Students in Classroom C: "))


desks_a = (a // 2) + (a % 2)
desks_b = (b // 2) + (b % 2)
desks_c = (c // 2) + (c % 2)

print(desks_a + desks_b + desks_c)