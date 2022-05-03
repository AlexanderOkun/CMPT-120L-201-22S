#Lab 4
#Alexander Okun
#Professor Kippins

#Swap Letter Case in Strings
import math


sample_string = "HeY thERe HowS iT GoING"
newString = sample_string.swapcase()
print(newString)


#center Strings with dashes
sample_string = "Hey There"
lengthOfString = len(sample_string)
length = lengthOfString + 8
newString = sample_string.center(length, "-")
print(newString)


#PARTITION a string
sample_string = "abcdefg.hijklmnop"
newString = sample_string.partition(".")
print(newString)

#Power Function
import math

num = int(input("Type in a number. "))
power = int(input("Type in what power you want to raise your other number to. "))
returnNumber = math.pow(num, power)
print(returnNumber)


#List frequency program
import collections

newList = [2,3,5,2,3,6,7,8,2]
frequency = collections.Counter(newList)

print(newList)
userNumber = int(input("Pick a number from the list above to find the frequency of the number in the lsit. "))

for item in newList:
    if item == userNumber:
        print(frequency.values)


#Slope Function
def division(x, y):
    return x / y

def subtraction(x, y):
    return x - y

print("This is the Slope Formula Program, enter the following....")
num_x1 = int(input("Enter the value for x1. "))
num_x2 = int(input("Enter the value for x2. "))
num_y1 = int(input("Enter the value for y1. "))
num_y2 = int(input("Enter the value for y2. "))

yValue = subtraction(num_y2, num_y1)
xValue = subtraction(num_x2, num_x1)
slope = division(yValue, xValue)
print("The slope of your given values is", slope)


#Distance Formula
import math

def addition(x, y):
    return x + y

print("This is the distance formula program, enter the following....")
num_x1 = int(input("Enter the value for x1. "))
num_x2 = int(input("Enter the value for x2. "))
num_y1 = int(input("Enter the value for y1. "))
num_y2 = int(input("Enter the value for y2. "))

xValue = subtraction(num_x2, num_x1)
yValue = subtraction(num_y2, num_y1)
new_xValue = math.pow(xValue)
new_yValue = math.pow(yValue)
val = addition(new_xValue, new_yValue)
distance = math.sqrt(val)
print("The distance of your given values is", distance)