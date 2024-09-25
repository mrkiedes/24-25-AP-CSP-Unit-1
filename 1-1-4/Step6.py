#   a114_divisible.py

# get two numbers from user
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# loop while the numbers are not divisible (the remainder is not 0)
while num1 % num2 != 0:

    # inform user of result
    print("Your numbers are not evenly divisible")

    # gather user input again
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

# inform user of result
print("Success, your numbers divide into each other")