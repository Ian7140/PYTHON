# String
sentence = 'I am a student'
print(sentence)
sentence2 = "Python is easy"
print(sentence2)
sentence3 = """ I'm a student and Python is easy """
print(sentence3)

# Slicing
jumin = "070718 - 1234567"
print("Gender : " + jumin[9])
print("Year : " + jumin[0:2]) #0부터 2직전까지
print("Birthday : " + jumin[2:6])
print("When? : " + jumin[:6]) #처음부터 6직전까지
# print("Rest : " , jumin[9:16])
print("Rest : " , jumin[9:]) #9번째부터 끝까지
print("Rest (Reverse) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

# String Function
python = "Python is Amazing"
print(python.lower()) # 소문자로 변환
print(python.upper()) # 대문자로 변환
print(python[0].isupper()) #소,대문자 확인
print(len(python)) # 길이 변환
print(python.replace("Python" , "Java")) #문자열에서 Python부분을 Java로 바꿈

index = python.index("n")
print(index) #첫번째 N위치
index = python.index("n", index + 1)
print(index) #두번째 N위치

# print(python.index("Java"))  오류발생
print(python.find("Java")) # 값이 없으면 -1 출력

print(python.count("n")) #n이 총 몇 번 나오는지 출력

# String Output Format
# print("a"+"b")
# print("a","b")

# Solution 1
print("I'm %d years old" % 20)
print("I like %s" % "Python")
print("Apple starts with %c" % "A")
print("I like %s and %s" %("Blue","Red"))

# Solution 2
print("I'm {} years old" .format(20))
print("I like {} and {}" .format("Blue","Red"))
print("I like {0} and {1}" .format("Blue","Red"))
print("I like {1} and {0}" .format("Blue","Red"))

#Solution 3
print("I'm {age} years old and love {color} color" .format(age = 20 , color = "Blue"))

# Solution 4
age = 20
color = "Blue"
print(f"I'm {age} years old and love {color} color")

# Etc
print("백문이 불여일견\n백견이 불여일타")
print("나는 \"이안\" 입니다") # 문장 내에서 따옴표로 사용 가능
print("hello\\Ian") # \\ : 문장 내에서 \
print("Red Apple\rPine") # 커서를 맨 앞으로 이동
print("Redd\bApple") # \b : backspace (한 글자 삭제)
print("Red\tApple") # \t : tab

#QUIZ 3

address = "http://naver.com"
password = address[7:12]
print(password[:3] + str(len(password)) + str(address.count("e")) + "!")
# The code above (I wrote it by the way.) isn't available when the address changes. 

my_str = address.replace("http://" ,"")
my_str = my_str[:my_str.index(".")] # 처음부터 '.'이 나오는 index 직전까지 자르기
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(pw)















