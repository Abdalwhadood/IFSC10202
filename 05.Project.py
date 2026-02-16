
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Special numbers in the range are:")

for num in range(start, end + 1):
    temp = num
    digits = 0
    
    while temp > 0:
        temp //= 10
        digits += 1
    
    temp = num
    sum_of_powers = 0
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** digits
        temp //= 10
    
    if sum_of_powers == num:
        print(num)
