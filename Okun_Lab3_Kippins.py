#Lab 3
#Alexander Okun
#Professor Kippins


#If,Elif, Else statement
odd_even_finder = int(input("Type a number so I can determine if it's odd or even. "))

if (odd_even_finder % 2) == 0:
    print("The number you typed in was even.")
elif (odd_even_finder % 2) == 1:
    print("The number you typed in was odd.")
else:
    print("You did not type a number in, rather a word. ")


#For Loop
for value in range(0, 10):
    print(value)


#For Loop with List
arr = ['Blue', 'Yellow', 'Red', 'Green', 'Purple', 'Magenta', 'Lilac']

for item in arr:
    print(item)
size = len(arr)
print(size)


#While Loop
program_addition = 1

while program_addition != 7:
    print("This is the", program_addition, "time the program has ran.")
    program_addition = program_addition + 1


#Function that adds 2 numbers
if True:
    num1 = int(input("Please enter a number. "))
    num2 = int(input("Please enter a second number." ))
    print("The total of your two numbers is", num1+num2)


#Initializing the Class
class Dog(object):
    def __init__(self, name: str, height: int, weight: int, breed: str):
        self.name = name
        self.height = height
        self.weight = weight
        self.breed = breed

    def info(self):
        print("Name:", self.name)
        print("Weight:", str(self.weight) + " Pounds")
        print("Height:", str(self.height) + " Inches")
        print("Breed:", self.breed)

if __name__ == "__main__":
    TheDog = Dog("Ruffles",90,30, "German Shepherd")
    TheDog.info()
    print(TheDog.name)