# get the factors of a number and determine if each is odd or even
#checking the factors of the number

number = int(input("Please Enter a Number: "))

value = 1
print("Factors of a Given Number {0} are:".format(number))

while (value <= number):
    if(number % value == 0):
        print("{0}".format(value))
    value = value + 1

# even or odd number
if (number % 2) == 0:
    print("even number")
else: 
    print("odd number") 

