start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Perfect numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num < 2:
        continue
    sum_of_divisors = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    if sum_of_divisors == num:
        print(num)