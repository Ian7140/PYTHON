# List
subway = [10,20,30]
print(subway)

subway = ['Ashely' , 'Jake' , 'Emma']
print(subway)

#Where is Jake?
print(subway.index("Jake"))

#Rohn got on the subway
subway.append("Rohn")
print(subway)

#Lily took the subway between 'Ashely' and 'Jake'
subway.insert(1,"Lily")
print(subway)

#Getting off
print(subway.pop())
print(subway)

#Checking the same names
subway.append("Ashely")
print(subway)
print(subway.count("Ashely"))

#Sorting is also available
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#Reverse
num_list.reverse()
print(num_list)

#Delete
num_list.clear()
print(num_list)

#다양한 자료형 사용가능
num_list = [5,2,4,3,1]
mix_list = ["Ian",20,True]
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)

#---------------------------------------------

#Dictionary
cabinet = {"A-3":"Mia" , "B-2":"Ember"}
# print(cabinet[100])
# print(cabinet[3])

print(cabinet.get(3))
# print(cabinet[5]) 값이 없기때문에 오류 발생 , 프로그램 종료
print(cabinet.get(5)) #값이 없기때문에 None 출력, 프로그램 진행
print("hi")

print(3 in cabinet) #True
print(5 in cabinet) #False
print(cabinet)

#Add Key and Value
cabinet["A-3"] = "Charles"
cabinet["C-34"] = "Haley"
print(cabinet)

#Delete
del cabinet["A-3"]
print(cabinet)

# Print keys & values
print(cabinet.keys())
print(cabinet.values())


#Both of them
print(cabinet.items())

#Clear
cabinet.clear()
print(cabinet)

#---------------------------------------------

#Tuple (내용변경,추가 불가능 / 속도가 빠름)
menu = ("Salmon" , "Tuna")
print(menu[0])
print(menu[1])

# menu.add("Chips") 에러발생

name = "Ian"
age = 17
hobby = "coding"
print(name,age,hobby)

(name , age, hobby) = ("Ian",17,"coding")
print(name,age,hobby)

#---------------------------------------------

#Set (집합)
#중복 불가능 / 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"Ian" , "Chloe", "Katy"}
python = set(["Ian" , "Tina"])

#교집합
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합 (only java)
print(java - python)
print(java.difference(python))

#Add value
python.add("Philip")
print(python)

#Delete Value
java.remove("Katy")
print(java)

#---------------------------------------------

menu = {"coffee","milk","juice"}
print(menu,type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#---------------------------------------------

#QUIZ 4
from random import *
users = range(1,21) #1부터 20까지 숫자생성
users = list(users) #범위가 range가 되면 list처럼 사용할 수 없기 때문에 자료형 변환
shuffle(users)
winners = sample(users,4)
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하합니다 --")

