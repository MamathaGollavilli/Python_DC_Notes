age = int(input("Enter your age: "))
if(age>=18):
    print("You are eligible to vote")
elif(age>0 and age<18):
    print("You are NOT eligible to vote")
    print("You have",18-age,"years left")
else:
    print("Invalid age")
