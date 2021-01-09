## Write a program that reads a number and displays the square, cube, and forth power.
import math

# reads a number
num = input("Input number: ")

# print the square, cube, and forth power
print("The square of " + num + ": %.2f" %(math.pow(float(num),2)))
print("The cube of " + num + ": %.2f" %(math.pow(float(num),3)))
print("The forth power of " + num + ": %.2f" %(float(num)**4))
