#표준출력
print("Python" , "Java" , "JavaScript" ,sep=",", end="?")
print("Which one is funny?")
# end : 문장의 끝을 설정한 기호로 만들기 + 뒤에 있는 문장 연결

import sys
print("Python","Java",file=sys.stdout) #표준출력
print("Python","Java",file=sys.stderr) #표준에러

scores = {"math" : 0, "coding" : 100 , "english" : 50}
for subject, score in scores.items():
    # print(subject , score)
    print(subject.ljust(8) , str(score).rjust(4), sep = ":")


for number in range(1,21):
    print("waiting list : " + str(number).zfill(3))

#---------------------------------------------

#표준입력
answer = input("Anything is fine : ") #이때 입력받는 값은 문자열이다
print(answer)

#---------------------------------------------

#다양한 출력포멧
print("{0: >10}".format(500)) # 빈 자리는 빈공간 , 오른쪽 정렬, 10자리 공간 확보
print("{0: >+10}".format(500)) #양수일 때  +, 음수일 때 -
print("{0:_<+10}".format(500)) #왼쪽 정렬하고 빈칸으로 _ 채우기
print("{0:,}".format(1237726346)) #3자리마다 , 찍어주기
print("{0:+,}".format(100000000)) #3자리마다 , 찍고 부호 붙이기
print("{0:^<+30,}".format(7344717283))
print("{0:f}".format(453/39)) #소수점 출력
print("{0:.2f}".format(37/2)) #소수점 3번째 자리에서 반올림

#---------------------------------------------

#파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
print("math : 0", file=score_file)
print("english : 50", file=score_file)
score_file.close()

score_file = open("score.txt","a",encoding="utf8")
score_file.write("science : 80")
score_file.write("\ncoding : 100")
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline()) #한 줄 읽고 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()

#---------------------------------------------

#Pickle : 데이터 -> 파일
import pickle
profile_file = open("profile.pickle","wb")
profile = {"Name" : "Ian" , "Age" : 17 , "Hobby" : ["Reading","Anime","Coding"]}
print(profile)
pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

#---------------------------------------------

#With
import pickle
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))
#파일을 닫을 필요없이 종료됨

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("Studying Python")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

#---------------------------------------------

#QUIZ 7
import pickle
for week in range(1,51):
    with open("{}주차.txt".format(week) , "w" , encoding="utf8") as report_file:
        report_file.write("- {}주차 주간보고 - ".format(week))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")

# "w"인 경우에는 덮어쓰기 가능

