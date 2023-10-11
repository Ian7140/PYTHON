# # 정수 (1~100) 1개를 입력받아 1부터 그 수까지 짝수의 합 구하기

# # number = int(input())
# sum = int(0)
# for i in range(2,number+1):
#     if i % 2 == 0:
#         sum += i

# print(sum)


# # 출석번호를 n번 무작위로 불렀을 때, 각 번호(1~23)가 불린 횟수를 각각 출력하기

# from random import *
# num = int(input())
# student = []
# student = list(map(int,input().split()))
# index = [0 for i in range(24)]
# for i in range(num):
#     index[student[i]] += 1
# for i in range(1,24):
#     print(index[i] , end=" ")


#바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
#n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

# baduk = [[0 for j in range(19)] for i in range(19)]
# white_baduk = int(input())
# for count in range(white_baduk):
#     x,y = map(int,input().split())
#     baduk[x][y] = 1

# for i in range(19):
#     for j in range(19):
#         print(baduk[i][j], end="")
#     print()

# # 위 문제 -> 함수사용

table = [[0 for j in range(19)] for i in range(19)]

def input_baduk(x,y):
    table[x][y] = 1

def print_baduk():
    for i in range(19):
        for j in range(19):
            print(table[i][j] , end="") #출력문 신경쓰기
        print()

if __name__ == "__main__":
    baduk = int(input())
    for i in range(baduk):
        x,y = map(int,input().split())
        input_baduk(x,y)
    
    print_baduk()