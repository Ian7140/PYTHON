# Function

def open_account():
    print("new account created")

def deposit(balance,money):
    print("deposit completed. {} dollars." .format(balance+money))
    return balance + money
def withdrawl(balance,money):
    if balance >= money:
        print("withdrawl completed. {} dollars".format(balance-money))
        return balance - money
    else:
        print("withdrawl didn't completed. {} dollars".format(balance))
        return balance
def withdrawl_night(balance,money):
    comission = 100
    return comission, balance-money-comission
open_account()
balance = 0
balance = deposit(balance,1000)
balance = withdrawl(balance, 300)
balance = withdrawl(balance,2000)
comission, balance = withdrawl_night(balance,500)
print(comission, balance)

#---------------------------------------------

# Default
# def profile(name,age,language):
#     print("Name : {}\nAge : {}\nLanguage : {}" \
#           .format(name,age,language))


def profile(name,age=17,language="Python"):
    print("Name : {}\nAge : {}\nLanguage : {}" \
          .format(name,age,language))

profile("Ian")
profile("Tanya")

# Keyword Value
def profile(name,age,language):
    print(name,age,language)

profile(name="Ian",language="Python",age=17)
profile(language="Python",age=17,name="Tanya")

#---------------------------------------------

# 가변인자
# def profile(name,age,lang1,lang2,lang3,lang4):
#     print("name : {}\nage : {}\n".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4)

def profile(name,age,*language):
    print("name : {}\nage : {}\n".format(name,age), end=" ")
    for lang in language:
        print(lang,end = " ")
    print()

profile("Ian",17,"C","Python","Java","C++")
profile("Sally",17,"Swift")
profile("Tanya",17,"JavaScript","Next.js")

#---------------------------------------------

# 지역변수와 전역변수
gun = 10

def checkpoint(soliders):
    global gun # 전역변수
    gun -= soliders
    print("Left guns : {}".format(gun))

def checkpoint_ret(gun,soliders):
    gun = gun - soliders
    print("Left guns : {}".format(gun))
    return gun

print("{}".format(gun))
gun = checkpoint_ret(gun,2)
print("left guns : {}".format(gun))

#---------------------------------------------

#QUIZ 6

def std_weight(height, gender):
    if gender == "여자":
        return (height / 100) ** 2 * 21
    else:
        return (height / 100) ** 2 * 22
    
height = int(input("Height : "))
gender = input("Gender : ")
print("키 {}cm {}의 표준체중은 {}kg 입니다.".format(height, gender, round(std_weight(height , gender),2)))







