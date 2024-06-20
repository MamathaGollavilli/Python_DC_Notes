num = int(input("Enter a number to reverse: "))

reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"Reversed number is: {reversed_num}")