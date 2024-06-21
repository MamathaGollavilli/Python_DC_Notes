num = int(input("Enter a num: "))
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev*10 + digit
    num //= 10
print("Reversed no:", rev)
