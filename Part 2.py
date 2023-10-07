print(2**3) # 2^3 = 8
print(5%3) # 2
print(10//4) # 2
print(9//3) #3

print(3>4) # False
print(10>=7) # True

print(3 == 3) # True
print(8 + 4 == 12) # True
print(1 != 3) # True

print((3>0) and (5>3)) # True
print((3>0) & (3<5)) # True

print((3>0) or (3>5)) # True
print((3>0) | (3>5)) # True
print(5>4>7) # False

print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 16
print(max(3,5)) # 5
print(min(2,6)) # 2
print(round(3.13)) # 3
print(round(4.8)) # 5

from math import *
print(floor(4.99)) # 4 (내림)
print(ceil(3.14)) # 4 (올림)
print(sqrt(16)) # 4 (제곱근)

from random import *
print(random()) # 0.0 ~ 1.0미만 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0미만 임의의 값 생성
print(int(random())) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1,46)) # 1 ~ 46미만의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45이하의 임의의 값 생성

#QUIZ 2

from random import *
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일로 선정되었습니다.")