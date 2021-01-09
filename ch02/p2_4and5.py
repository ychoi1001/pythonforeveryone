## Write a program that prompts the user for two integers and then prints
# - The sum
# - The difference
# - The product
# - The average
# - The distance (absolute value of the difference)
# - The maximum (the larger of the two)
# - The minimum (the smaller of the two) #

# reads two numbers
num1 = float(input("Input first num: "))
num2 = float(input("Input second num: "))

# display result
print("%-11s %6d" %("Sum:", num1+num2))
print("%-11s %6d" %("Difference:", num1-num2))
print("%-11s %6d" %("Product:", num1*num2))
print("%-11s %9.2f" %("Average:", (num1+num2)/2))
print("%-11s %6d" %("Distance:", abs(num1-num2)))
print("%-11s %6d" %("Maximum:", max(num1,num2)))
print("%-11s %6d" %("Minimum:", min(num1,num2)))
