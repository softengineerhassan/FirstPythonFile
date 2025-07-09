#Operators, Input/Output, and Type Conversion
firstName = input("enter your first name: ")
lastName = input("enter your last name")
print("your full name is: "+firstName +" "+ lastName)

num1 = int(input("enter number"))
num2 = int(input("enter another number"))
sum = num1+num2
print("the total number is"+str(sum))

# for and while loop
for i in range(1,11):
    print(i)

for i in range(1,5):
    if i%2==0:
        print(i)

for i in range(1,6):
    if i%2==0:
        print(i+1)

userInput = int(input("enter a number"))
total = 0
for i in range(1, userInput + 1):
    total = total + i
print(total)

uinput = int(input("enter a number"))
for i in range(1,11):
    print(f"{uinput} x {i} = {uinput*i}")

num1 = int(input("enter numbers"))
count = 0
while num1>0:
    num1 //= 10
    count +=1
print("total numbers: ",count)

num = int(input("enter numbers"))
fact = 1
for i in range(1, num+1):
    fact*=i
print(fact)

usern = int(input("enter number"))
rev = 0
while usern>0:
    digit = usern % 10
    rev = rev * 10 + digit
    usern //= 10
print(rev)

n = int(input("enter any numbers"))
rev = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n //=10
print(rev)

n = int(input("enter number of rows"))
for i in range(1, n+1):
    print("*"*n)

secret = 9
guess = -2
tries = 0
while guess != secret:
    guess = int(input("guess the number:"))
    tries = tries + 1
print(f"Correct! It took you {tries} tries.")

# if/elif/else
numb = int(input("enter a number"))
if numb<0:
    print("its a negative number:")
elif numb==0:
    print("its a zero number:")
else:
    print("it is a positive number:")

user1 = int(input("enter a number"))
if user1%2==0:
    print("it is a even number")
else:
    print("it is a odd number")

num1 = int(input("enter number"))
num2 = int(input("enter number"))
num3 = int(input("enter number"))
if num1>num2 and num1>num3:
    print("numb1 is greatest number: ", num1)
elif num2>num1 and num2>num3:
    print("numb2 is greater number", num2)
elif num3>num1 and num3>num2:
    print("num3 is greater number:", num3)
else:
    print("end")

year = int(input("enter year"))
if year%4==0 and year%100!=0 or (year%400==0):
    print("the year is leap year")
else:
    print("it is not a leap year")

ch = input("enter a charactar").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in "aeiou":
        print(f"{ch} is a vowel")
    else:
        print("is not a vowel")
else:
    print("please enter single charactar")

age = int(input("enter age"))
if age >=0 and age <=12:
    print("your age group is child")
elif age >=13 and age <=19:
    print("your age group is teen")
elif age >= 20 and age <=59:
    print("your age group is adult")
elif age>60:
    print("you are a senior")
else:
    print("enter a valid age")

numb1 = int(input("enter number1:"))
numb2 = int(input("enter number2:"))
operator = input("enter an operator: (-,+,/,*)")

if operator == "+":
    print(numb1+numb2)
elif operator == "-":
    print(numb1-numb2)
elif operator == "/":
    print(numb1/numb2)
elif operator == "*":
    print(numb1*numb2)

subject1 = int(input("enter marks of subject 1"))
subject2 = int(input("enter marks of subject 2"))
subject3 = int(input("enter marks of subject 3"))
avg = (subject1 + subject2 + subject3)/3
if avg>40 and subject1>33 and subject2>33 and subject3>33:
    print("pass")
else:
    print("fail")

n1 = int(input("enter a number:"))
if n1>=50 and n1<=100:
    print("yes this number lies between 50 and 100")
else:
    print("no this number is not lies between 50 and 100")

username = "Hassan@gmail.com"
password = 786787

useri = input("enter username")
userp = int(input("enter password"))
if useri==username and userp==password:
    print("login successfuly")
else:
    print("wrong credentianls")

unit = int(input("enter number of units"))
if unit<=100:
    unit*=0
    print("cost of units is",unit)
elif unit>100 and unit<=200:
    unit*=5
    print("cost of units is",unit)
elif unit>200:
    unit*=10
    print("cost of units is",unit)
else:
    print("enter correct number of units")

per = int(input("enter marks percentage:"))
if per >= 90 and per <=100:
    print("A+")
elif per>=80 and per <90:
    print("A")
elif per>=70 and per <80:
    print("C")
else:
    print("fail")

def greet():
    print("Hello, Good moring, My name is Ali Hassan")
greet()

def greet(name):
    print(f"Hello, {name}")
greet("Hassan")

def add(a,b):
    return a+b
result = add(4,5)
print(result)

def greet(name="Hassan"):
    print(f"Hello {name}")
greet()

#Guesing number game!
