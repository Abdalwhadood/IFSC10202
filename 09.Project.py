
distances = []

input_file = open("09.Project Distances.csv", "r")

for line in input_file:
    line = line.strip()          
    if line != "":               
        row = line.split(",")    
        distances.append(row)    

input_file.close()


print()
for row in distances:
    for item in row:
        print(item.rjust(10), end="")   
    print()                          
print()


from_city = input("Enter From City: ")
to_city   = input("Enter To City: ")

from_index = -1    

for i in range(len(distances)):
    if distances[i][0].lower() == from_city.lower():   
        from_index = i
        break

to_index = -1

for j in range(len(distances[0])):
    if distances[0][j].lower() == to_city.lower():    
        to_index = j
        break


print()

if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = distances[from_index][to_index]
    print(from_city + " to " + to_city + " - " + distance + " miles")

print()
