# Reversing the order of words in the sentence "python is very easy"

str1 = "python is very easy"
ls = str1.split()
print(ls)
reversed = ls[::-1]
print(reversed)

# Reversing the order of words in the sentence "python is very easy" and then reversing each word individually.

str1 = "python is very easy"
ls = str1.split()
reversed = ls[::-1]
reversed_words = [word[::-1] for word in reversed]
print(reversed_words)

# Check if a list is empty or not:

lst = []
if not lst:
    print("List is empty")
else:
    print("List is not empty")

# Create a new list with the square of each element in the original list:

original_list = [1, 2, 3, 4]
squared_list = [x**2 for x in original_list]
print(squared_list)

# Remove all occurrences of a specific element from the list:

lst = [1, 2, 3, 2, 4, 2]
remove = 2
new_lst = [x for x in lst if x != remove]
print(new_lst)

# Check if a list is a palindrome:

lst = [1, 2, 3, 2, 1]
if lst == lst[::-1]:
    print("List is a palindrome")
else:
    print("List is not a palindrome")

# Calculate the product of elements in the list:

lst = [1, 2, 3, 4]
product = 1
for x in lst:
    product *= x
print(product)

# Check leap year:

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Find the factorial of a number:

num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)

# Check Armstrong number:

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# Printing largest, second largest and minimum number from a list

numbers = [10, 20, 4, 45, 99, 6, 18]
maximum = max(numbers)
minimum = min(numbers)
temp = numbers.copy()
temp.remove(maximum)
second_largest = max(temp)
print("Largest number is:", maximum)
print("Second largest number is:", second_largest)
print("Smallest number is:", minimum)

# Replace first and last element of list without using 3rd variable

numbers = [1, 2, 3, 4, 5]
if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("List after swapping first and last elements:", numbers)


