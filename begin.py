import calendar
import datetime
import time

print("Hello World")
print("Hello + World")
print("Hello"+"World")
print("Hello,World!")

s = 'Python'
# 访问第一个字符 P
print(s[0])
print(s[1:3])
print(s[1:2])
print(s[1])


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            return False
    return True


primes = [prime for prime in range(2, 101) if is_prime(prime)]
print(primes)

import time
t=time.localtime()
print('t-->',t)
print(t.tm_year)
print(t[0])
print(time.time())
print(time.gmtime())
print(time.localtime())
print(time.asctime(time.localtime()))
print(time.mktime(time.localtime()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.max)
print(datetime.date.min)
t=datetime.time(10,10,10)
print(t.isoformat())
print(t.replace(hour=9,minute=9))
print(t.strftime('%I:%M:%S %p'))
print(t.hour)
print(t.microsecond)
print(t.tzinfo)
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.min)

td=datetime.datetime.today()
print(td.date())
print(td.weekday())
print(td.isoweekday())
print(td.isocalendar())
print(td.isoformat())

import calendar
calendar.setfirstweekday(1)
print(calendar.firstweekday())
print(calendar.isleap(2023))
print(calendar.weekday(2024,6,13))
print(calendar.monthrange(2024,6))
print(calendar.month(2024,6))

from calendar import Calendar
c=Calendar()
print(list(c.iterweekdays()))
for i in c.itermonthdates(2024,6):
    print(i)

from calendar import TextCalendar
tc=TextCalendar()
print(tc.formatmonth(2024,6))



def my_empty():
    pass

def my_print(name):
    print("hello",name)

def my_sum(x,y):
    s = x + y
    print('s-->',s)
    return s


def my_variable(*params):
    for p in params:
        print(p)
my_sub = lambda x, y: x - y
my_empty()
my_print("Jhon")
resul=my_sum(1,2)
my_variable(1,2,3,4,5,6)
print(my_sub(2,1))

print("------------")
num_arr = [1,2,3,4,5,6,7,8,9,10]
s=0
for i in num_arr:
    if i% 2 == 0:
        s=s+i
print(s)

print("------------")
price = 10
print(price)
rating = 4.9
name = "Mosh"
is_published = True

full_nam = "John Smith"
age = 20
is_new = True

name = input(" What is your name? ")
color = input(" What is your favourite color? ")
input(name + " likes " + color)

birth_year = input("Birth year: ")
age = 2024 - int(birth_year)
print(age)

int()
float()
bool()

birth_year = input("Birth year: ")
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)

birth_year = input("Birth year: ")
age = 2024 - int(birth_year)
print(age)


Weight = input("Weight: ")
Weight_kg = float(Weight) / 2
print(Weight_kg)


Weight = input("Weight: ")
Weight_kg = float(Weight) / 2
text = "Kg="
result = text + str(Weight_kg)
print(result)




Weight = input("Weight: ")
Weight_kg = float(Weight) / 2
print(f"Kg={Weight_kg}")


course = "Python for Beginners"
print(course.upper())
print(course.replace("P","Y"))
print("python" in course)

import math

print(math.ceil(2.9))

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")



# price =1000000
# is_good = True

# if is_good:
#    print(price * 10 %)
# else:
#    print(price * 20 %)

price =1000000
is_good = True

if is_good:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"down_payment: ${down_payment}")


has_high_income = True
has_good_credit = False

if has_high_income and not has_good_credit:
    print("Eligible for loan")

temperature = 30
if temperature >= 35:
    print("It's a hot day")
else:
    print("It's not a hot day")


name_characters = 2
if name_characters < 3:
    print("name must be at least 3 characters")
elif name_characters > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

name = "J"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")




weight = int(input("Weight: "))
unit = input("(L)bs or (K)g:")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")


weight = int(input("Weight: "))
ww = input("(L)bs or (K)g:")
if ww.upper() == "L":
    ee = weight * 0.45
    print(f"You are {ee} kilos")
else:
    ee = weight / 0.45
    print(f"You are {ee} pounds")