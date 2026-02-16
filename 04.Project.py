
height = int(input("Enter maximum height: "))

for i in range(1, height + 1):
    for l in range(i):
        print("*", end=" ")
    print()

for i in range(height - 1, 0, -1):
    for l in range(i):
        print("*", end=" ")
    print()
