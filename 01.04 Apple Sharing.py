number_of_students = int(input("How Many Students are in your class: "))
number_of_apples = int(input("How many Apples are there: "))

print("\nNumber of Students:",number_of_students)
print("Number of Apples:",number_of_apples)

basket = number_of_students // number_of_apples

print(basket)

remains = number_of_students % number_of_apples
print(remains)
