#-*-coding:utf-8

print("# 반복문 while, for")
# 기존 언어의 while문과 기능과 사용법이 동일함
# while 문 외부에 카운트 변수를 선언, while 내부에 변수를 카운트, while 문 옆에 조건을 입력
# while의 조건 부분에 괄호를 사용하지 않음
# if 문과 동일하게 들여쓰기를 맞춰줘야함

treeHit = 0
while treeHit < 10:
    treeHit += 1 # 변수 카운트
    print("나무를 {0}번 찍었습니다.".format(treeHit))
    if treeHit == 10:
        print("나무 넘어갑니다.")

print()
print("# 반복문 탈출하기 (break)")
# break를 만나면 가장 가까운 반복문에서 탈출함
# 기존 언어의 break 문과 기능 및 사용법이 동일함
coffee = 10
money = 300
while money: # 숫자형은 0이 아니면 True 이므로 while을 실행함
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 {0}개입니다.".format(coffee))
    if not coffee: # coffee가 0일때 False. not coffee 이므로 True. if실행
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # 가장 가까운 반복문을 탈출

# 자바의 경우
# while(money > 0) {
#     System.out.println();

#     if (!coffee) {
#         break;
#     }
# }

print()
print("#커피 자판기")
# coffee = 10
# while True: # while의 조건문에 True를 입력하면 while의 반복 조건이 무조건 True이므로 while은 무한루프에 빠짐
#     money = int(input("돈을 넣어 주세요 : "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee -= 1
#     elif money > 300:
#         print("거스름돈 {0}를 주고 커피를 줍니다.".format(money-300))
#         print("남은 커피의 양은 {0}개 입니다.".format(coffee))
#         coffee -= 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 {0}개 입니다.".format(coffee))
#     if not coffee:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

print()
print("# 조건에 맞지 않을 경우 맨 처음으로 돌아가기 (continue)")
# 기존 다른 언어의 continue 문과 기능과 사용법이 동일함
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: 
        continue
    print(a)

print()
print('# 문제 2) 사용자가 입력한 숫자에 해당하는 구구단을 출력하세요')
# dan = int(input("단 : "))
# # 자바의 형변환과 다름
# # dan = (int)dan
# i = 2 # 카운트 변수 선언
# while i < 10:
#     print("{0} * {1} = {2}".format(dan, i, (dan * i)))
#     i += 1

print()
print("# 2중 while 문을 사용해서 구구단 전체를 출력하세요")
dan = 2
while dan < 10:
    print("{0}단".format(dan))
    i = 2
    while i < 10:
        print("{0} * {1} = {2}".format(dan, i, dan * i))
        i +=1
    dan += 1

print()
print("# 2중 while 문을 사용해서 구구단 전체를 출력하세요")
dan, i = (2, 2)
while dan < 10:
    print("{0}단".format(dan))
    while i < 10:
        print("{0} * {1} = {2}".format(dan, i, dan * i))
        i +=1
    i = 2
    dan += 1

# 자바의 경우
# dan = 2;
# while (){
#     i = 2;
#     while(){
#         i ++;
#     }
#     dan++;
# }

print()
print("# for")
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

print()
a = [(1,2), (3,4), (5,6)]

print()
print("# 문제4) while과 list를 사용하여 로또 번호 자동 생성 프로그램을 만드세요")
# 6개의 숫자를 랜덤으로 출력 받음
# 발생된 로또 번호를 리스트 변수 lotto에 저장
# 마지막에 리스트 lotto를 화면에 출력

# 난수 발생을 위한 모듈
import random
# 범위 내의 난수 발생
print('방법 1.')
val1 = random.randint(1, 45)
val2 = random.randint(1, 45)
val3 = random.randint(1, 45)
val4 = random.randint(1, 45)
val5 = random.randint(1, 45)
val6 = random.randint(1, 45)
lotto = [val1, val2, val3, val4, val5, val6]
print(lotto)
print()
print("방법2.")
lotto=[]
i = 0
while i < 6:
    val = random.randint(1, 45)
    lotto.insert(i, val)
    print(lotto[i])
    i += 1
    # j = 0
    if val - val ==0:
        i = 0
    # while j < 5:
    # #     if lotto[i] == lotto[j]:
    # #         i = 0
    #     print(lotto[j])
    #     j += 1
print(lotto)

print()
print("선생님 풀이")
lotto=[]#로또번호 받을 빈 리스트
i = 0#
while i < 6:
    val = random.randint(1, 45)
    lotto.append(val)
    i += 1
    if val - val ==0:
        i = 0
print(lotto)