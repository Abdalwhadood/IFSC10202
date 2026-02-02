def calculate_time_difference():
    print("Enter the first timestamp (the earlier time):")
    h1 = int(input("Hours: "))
    m1 = int(input("Minutes: "))
    s1 = int(input("Seconds: "))

    print("\nEnter the second timestamp (the later time):")
    h2 = int(input("Hours: "))
    m2 = int(input("Minutes: "))
    s2 = int(input("Seconds: "))

    # Convert everything to seconds
    total_seconds1 = (h1 * 3600) + (m1 * 60) + s1
    total_seconds2 = (h2 * 3600) + (m2 * 60) + s2

    # Calculate the difference
    difference = total_seconds2 - total_seconds1

    print(f"\nThere are {difference} seconds between the two timestamps.")

if __name__ == "__main__":
    calculate_time_difference()