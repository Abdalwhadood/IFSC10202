km = float(input("Enter the length of the race in kilometers: "))

minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

miles = km / 1.61

total_seconds = (minutes * 60) + seconds
hours = total_seconds / 3600

mph = miles / hours

print(f"Your average speed was {mph:.2f} miles per hour.")