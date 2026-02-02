total_seconds = int(input("Enter a length of time in seconds: "))

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR
SECONDS_PER_YEAR = 365 * SECONDS_PER_DAY

years = total_seconds // SECONDS_PER_YEAR
total_seconds % SECONDS_PER_YEAR

days = total_seconds // SECONDS_PER_DAY
total_seconds % SECONDS_PER_DAY

hours = total_seconds // SECONDS_PER_HOUR
total_seconds % SECONDS_PER_HOUR

minutes = total_seconds // SECONDS_PER_MINUTE
seconds = total_seconds % SECONDS_PER_MINUTE

print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
