# 1번 문제

def f(number):
    global num
    if number == num:
        return num
    else:
        f(number+1)
        print(number,end=" ")

num = int(input())
print(num,end=" ")
f(1)
print("\n")

# 2번 문제
def f(num):
    global sum
    global numbers
    if num:
        f(num-1)
        sum += numbers.pop()
    else:
        return
    
numbers = list(map(int,input().split()))
sum = int(0)
f(len(numbers))
print(sum)


# 3번 문제

def max_value(b):
    global numbers
    global biggest
    if biggest < numbers[b-1]:
        biggest = numbers[b-1]
        max_value(b-1)
    if b < 0:
        return
    

numbers = list(map(int,input().split()))
biggest = int(-100)
max_value(len(numbers))
print(biggest)
