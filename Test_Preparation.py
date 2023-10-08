# # 정수 (1~100) 1개를 입력받어 1부터 그 수까지 짝수의 합 구하기

num = int(input("정수를 입력하세요 : "))
count = 0
for i in range(1,num+1):
    if i%2 == 0:
        count += i
print(count)

# # 리스트 예제 1
# # 출선번호를 n번 무작위로 불렀을 때, 각 번호(1~23)가 불린 횟수를 각각 출력하기

student = [0 for i in range(24)]
count = []
num = int(input())
count = list(map(int,input().split())) #헷갈린 부분
for i in range(num):
    student[count[i]]+=1
for i in range(1,24):
    print(student[i], end=" ")
print("\n")


# # 리스트 예제 2

baduk = [[0 for j in range(19)] for i in range(19)] #2차원 배열 선언 기억하기
count = int(input())
for _ in range(count):
    x,y = map(int, input().split())
    baduk[x][y] = 1

for i in range(19):
    for j in range(19):
        print(baduk[i][j] , end="")
    print()


# # 리스트 예제 2 (함수사용)

def white(x,y):
    baduk[x][y] = 1

baduk = [[0 for j in range(19)] for i in range(19)]
num = int(input())
for i in range(num):
    x,y = map(int,input().split())
    white(x,y)

for i in range(19):
    for j in range(19):
        print(baduk[i][j],end="")
    print()

# 재귀함수

num = int(input())
stair = [ int(input()) for i in range(num)] 
dp = [0] * (num) #리스트를 num의 길이만큼 0으로 초기화
if len(stair) <= 2: #계단이 2개 이하인 경우
    print(sum(stair))
elif num >= 3:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2,num):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])
