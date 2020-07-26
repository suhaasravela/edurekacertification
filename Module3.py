# Question 1
import math

x, y = 0, 0

while True:
    step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")

    if step == "":
        break

    else:
        step = step.split(" ")

        if step[0] == "UP":
            y = y + int(step[1])
        elif step[0] == "DOWN":
            y = y - int(step[1])
        elif step[0] == "LEFT":
            x = x - int(step[1])
        elif step[0] == "RIGHT":
            x = x + int(step[1])

c = math.sqrt(x**2 + y**2)

print("Distance:", c)

# Question 2
string = input("Enter list of items (comma seperated)>>> ")
find_ele = input("Enter the elements which needs to find>>> ")

list_eles = str(string).split(",")

if find_ele in list_eles:
    print(f"{find_ele} is present in given list at position {list_eles.index(find_ele)+1}")
else:
    print(f"{find_ele} is not present in given list")

# Question 3
import time
sample data: (timezone= utc/zulutime)
    timestamps = ['2015-03-25 21:15:00', '2015-06-27 18:24:00', '2015-06-27 18:22:00', '2015-06-27 18:21:00', '2015-07-07 07:53:00']

    for timestamp in timestamps:
        time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        hr, mi = (time.hour, time.minute)
        if hr>=7 and hr<18: print ("daylight")
        else: print ("evening or night")

# Question 4
from math import radians, sin, cos, acos

print("Input coordinates of two points:")
slat = radians(float(input("Starting latitude: ")))
slon = radians(float(input("Ending longitude: ")))
elat = radians(float(input("Starting latitude: ")))
elon = radians(float(input("Ending longitude: ")))

dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
print("The distance is %.2fkm." % dist)

#Question 5
def CashWithdrawal():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def CashCredit():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        AMT=input('Enter Amount That You Wish to Credit To Bank:')
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def ChangePassword():
    PIN=input('Enter ATM or CARD PIN to proceed:')
    if PIN==123:
        OLD_PWD=raw_input('Please Enter Your Old Password:')
        print '***Thank You For Banking With Us***'
    else:
        print 'You Have Enterd Invalid PIN. Try Again'

def Main():
    print 'Welcome to XYZ Bank\nChoose from below options'
    print '1. Case withdrawal\n2. Cash credit\n3. Change password'
    opt=input('Enter your option:')
    if opt==1:
        CashWithdrawal()
    if opt==2:
        CashCredit()
    if opt==3:
        ChangePassword()

Main()

# Question 6: 
for i in range(2000, 3201):
    if(not i%7 and i%5):
        print(i, end=", ")

# Question 7: 
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

# Question 8: 
import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)

# Question 9: 
from numpy import fromfunction as ff

x,y = (3,5)
arr = ff(lambda x,y:x*y,(x,y))
print(arr)


arr = [[i*j for j in range(y)]for i in range(x)]


print()
[print(row) for row in arr]

# Question 10: 
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

# Question 11: 
lines = []
while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for l in lines:
    print(l)

# Question 12: 
phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))

# Question 13: 
items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print(','.join(items))

# Question 14
phrase = input("Type in: ")
phrase = list(phrase)

u, l = 0, 0
for i in phrase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER:", u)
print("lower:", l)

# Question 15: 
import math 
 
print(math.fsum(range(10))) 


