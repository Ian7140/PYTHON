# If
weather = input("How's the weather? ")
if weather == "rain" or weather == "snow":
    print("Don't forget an umbrella")
elif weather == "dust":
    print("Don't forget to take a mask")
else:
    print("No Needed")


temp = int(input("How's the temperature? "))
if 30 <= temp:
    print("Isn't it too hot?")
elif 10 <= temp and temp < 30:
    print("It's fine")
elif 0 <= temp and temp < 10:
    print("Where's your coat?")
else:
    print("It's Freezing")

#---------------------------------------------

# For

for waiting_no in range(1,6): 
    print("대기번호 : {0}" .format(waiting_no))

starbucks = ["Danny" , "Rose", "Leo"]
for customer in starbucks:
    print("{}, your coffee is ready" .format(customer))


#---------------------------------------------

# While

customer = "Leo"
index = 5
while index >= 1:
    print("{},your coffee is ready. {} time(s) left".format(customer,index))
    index -= 1
    if index == 0:
        print("Coffee will be disposed")

# customer = "Rose"
# index = 1
# while True:
#     print("{},your coffee is ready. {} time(s)".format(customer,index))
#     index += 1

customer = "Danny"
person = "Unknown"

while person != customer:
    print("{}, your coffee is ready" .format(customer))
    person = input("What's your name? ")


#---------------------------------------------

# Continue and Break
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent :
        continue
    elif student in no_book:
        print("Class Over")
        break
    print("{}, it's your turn" .format(student))

#---------------------------------------------

# 한 줄 for

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Veky", "Ken", "Ruby"]
students = [len(i) for i in students]
print(students)

students = ["Veky", "Ken", "Ruby"]
students = [i.upper() for i in students]
print(students)

#---------------------------------------------

#QUIZ 5
from random import *
count = int(0)
for i in range(1,51):
    min = randint(5,50)
    if min >= 5 and min <= 15:
        print("[O] {}번째 손님 (소요시간 : {}분)" .format(i,min))
        count += 1
    else:
        print("[ ] {}번째 손님 (소요시간 : {}분)" .format(i,min))

print("총 탑승 승객 : {}분" .format(count))






