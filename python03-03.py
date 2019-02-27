#-*-coding:utf-8
import random

print("# for 문 사용하기")
# 기존 언어의 for 문과 다른 for ~ in 문의 형태를 하고 있음
# Java 에서는 for ~ in 문과 같고 C#에서는 foreach 문과 같은 형태의 반복문
# for 문의 조건절에 in 연산자를 사용하여 해당하는 리스트 및 튜플, 딕셔너리의 모든 요소를 카운트 변수 없이 출력할 수 있음
# for 문 사용시 괄호를 사용하지 않음

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 리스트 a의 요소가 튜플로 구성되어 있어 in 연산자에서 리스트의 값을 받는 부분을 튜플로 지정해야함
# 튜플로 변수 선언 및 초기화 하는 방식인 (a, b) = (값1, 값2)을 사용하여 리스트 a의 요소 데이터를 대입받음
print()
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)
# (a, b) = (3, 4)
print(first, last)

# print()
# print('# 문제 1) 랜덤 숫자를 받아 그에 해당하는 구구단을 출력하세요')
# val = random.randint()

print()
print("# 문제 1) 1 ~ 10 까지의 합을 구하는 프로그램을 for문을 사용하여 만드세요")
a=[]
i=1
b=0
while i <= 10:
    a.append(i)
    i+=1
for i in a:
    print("1 ~ 10까지 출력 : {0}".format(i))
    b = b + i
print("1 ~ 10까지의 합 : {0}".format(b))

print()
print("# 수영씨 풀이")
a=[1]
b=0
for i in a:
    while i <= 10:
        b = b + i
        i +=1
print(b)

print()
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("{0}번 학생은 합격입니다.".format(number))
    else:
        print("{0}번 학생은 불합격입니다.".format(number))

print()
print("# for문에서 continue 사용")
# while문 에서의 continue 사용법과 동일함
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("{0}번 학생 축하합니다. 합격입니다.".format(number))

print()
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        break
    print("{0}번 학생 축하합니다. 합격입니다.".format(number))

print()
print("# for 문과 range() 함수 사용하기")
# range() 함수는 지정한 범위의 숫자의 리스트를 자동 생성
# range(시작숫자, 끝숫자), 시작 숫자를 제외하면 0에서 지정한 끝 숫자까지 자동 생성
print(range(10))
print(range(1, 11))

sum = 0
for i in range(1, 11):
    sum += i
print(sum)

print()
marks = [90, 25, 67, 45, 80]

print()
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print()

print()
print("# 문제 2) 사용자 입력을 받아 해당하는 단수의 구구단을 출력하세요")
# dan = input("출력할 구구단을 입력하세요 : ")
# dan = int(dan)
dan =5
for i in range(1, 10):
    print(dan * i, end = " ")
# print() 함수의 끝은 \n이 붙어있음
# print(dan * val, end="\n")
# end를 사용하게 되면 끝나는 부분에 다른 문자를 입력할 수 있음

print()
print("# 리스트 내포 사용하기")
# 리스트에 for ~ in 문을 사용하여 리스트의 요소를 자동 생성하는 방식
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

print()
print("# 리스트 내포 방식")
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

print()
result = [num * 3 for num in a if num % 2 == 0]
print("리스트 내포방식 for, if 사용 : {0}".format(result))

print()
print("# 문제 3) listNum 이라는 리스트에 숫자가 1부터 10까지 들어있다. 이 리스트를 리스트 내포 방식을 사용하여 복사하세요")
# 복사 받을 리스트의 이름 : listCopy
listNum = range(1, 11)
print(listNum)
listCopy = [num for num in listNum]
print("원본 리스트 listNum : {0}".format(listNum))
print("사본 리스트 listCopy : {0}".format(listCopy))

print()
print("# 리스트 안에 포함된 2중 for문")
result = [x*y for x in range(2,10)
    for y in range(1,10)]
print(result)