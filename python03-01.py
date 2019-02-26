#-*-coding:utf-8

print('< if 문 >')
# 기존 언어의 if문과 거의 동일함
# if (조건문) {
#   실행할 코드
# }

# 파이썬은 조건문 부분에 괄호가 없음
# 파이썬은 코드 블럭 대신 : 기호를 사용함
# 실행할 코드 부분의 들여쓰기를 반드시 해야함 (중요)
# 파이썬에서 들여쓰기 부분이 다르면 실행 오류가 발생함
# if ~ else if ~ else 문의 경우 else if 의 명령어가 elif로 되어 있음(사용하는 방법은 동일)

# 파이썬은 코드 블럭을 사용하지 않기 때문에 실행 코드 영역을 확인할 방법이 없음
# 실행 코드의 영역을 구분하는 방법이 바로 들여쓰기 임
# 이러한 이유로 인하여 들여쓰기 부분을 통일해야 함

# 이렇게 들여쓰기를 통한 소스의 제어는 다른 사람들과의 협업시 모두 동일한 패턴의 소스로 개발이 가능하기 때문에 프로그램의 유지 보수가 쉬움

money = 1
# print("타고") 부분이 윗라인과 들여쓰기 부분이 다르지만 오류가 발생하지 않은 이유는 print("타고") 부분은 if문 밖에 있는 print 문으로 인식되기 때문
if money:
    print("택시를")
print("타고")

print()
# print("가자") 부분에서 오류가 발생하는 이유는 if문 내부에 존재하는 print 문이지만 다른 문장들과 들여쓰기 위치가 맞지 않기 때문
money = 1
if money:
    print("택시를")
    print("타고")
        # print("가자")

print()

print('# 비교 연산자')
# 기본 비교 연산자 <, >, <=, >=, ==, !=
# 다른 언어의 비교 연산자와 동일함
x = 3
y = 2
print('x > y : {0}'.format(x > y))
print('x < y : {0}'.format(x < y))
print('x == y : {0}'.format(x == y))
print('x != y : {0}'.format(x != y))

print()
print('# 파이썬의 and, or, not, in 연산자')
# 자바 : && (and), || (or), !(not)
# 기존 다른 언어에서 사용하는 방법고 동일하지만 연산자 기호가 영문자로 변경됨
# if (a > 5 && a < 10){
# }
a = 8
if a > 5 and a < 10:
    print("a는 5보다 크고 10보다 작다")

if a > 0 or a < 10:
    print("a는 0보다 크거나 10보다 작다")

if a is not 10:
    print("a는 10과 같지 않다")

# in 연산자
# 리스트나 튜플, 문자열 안에 지정한 데이터가 있는지 확인하는 연산자
# if 문과 사용할 경우에는 해당 리스트나, 튜플, 문자열에 지정한 데이터가 있는지 확인하는 용도로 사용
# for 문에서 사용할 경우 해당 리스트나 튜플, 딕셔너리에서 처음부터 끝까지의 요소를 하나씩 꺼내오는 용도로 사용

a = [1, 2, 3]

if (2 in a):
    print("리스트 a에 숫자 2가 포함되어 있음")
    
for value in a:
    print(value)

money = 2000
card = 1
if money >= 3000 or card:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

print()
print('# x in s, x not in s')

print("1 은 리스트 [1, 2, 3]에 포함되어 있음 : {0}".format(1 in [1, 2, 3]))
# not 연산자와 in 연산자를 함께 사용하여 원래의 의미와 반대로 동작하도록 함
# in과 not in은 주로 if 문에서 사용함
print("1 은 리스트 [1, 2, 3]에 포함되어 있지 않음 : {0}".format(1 not in [1, 2, 3]))

print()
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

print()
print('#pass')
# 반복문에서 사용하는 continue와 비슷한 기능을 가진 명령어로 if문에서 특별한 작업을 하지 않을 경우 사용
# 기존 언어에서는 if 문에서의 실행햐야할 코드 부분을 코드 블럭으로 감싸고 있는 형태이기 때문에 실행 되어야 할 영역이 명확함
# 실행 되어야 하는 영역이 명확하기 때문에 코드블럭 내에 아무런 실행코드가 없어도 오류가 발생하지 않음
# 파이썬은 if 문 내에 아무런 실행코드가 없을 경우 의도적으로 실행코등의 입력이 없는 것인지 아닌지를 판단할 수 없기에 (코드 블럭 대신 들여쓰기를 
# 통하여 구분하기 때문) pass 라는 명령어를 사용하여 어떠한 실행도 하지 않는다고 명시함
if 'money' in pocket:
    pass
else:
    print('걸어가라')

print()
print("# elif 문")
# 파이썬에서는 기존 언어의 if ~ else if ~ else 문을 elif문을 표현함
# 사용 방법은 기존 언어의 if ~ else if ~ else와 동일함
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card: # 숫자형은 0이 아니면 무조건 True
    print("버스를 타고 가라")
else:
    print("걸어 가라")

print()
print('# 문제 1) 성적표를 출력하는 프로그램을 작성하세요')
# 조건 1. 95 이상 A+, 90 이상 A, 85 이상 B+, 80 이상 B 형태로 해서 60이하는 F로 표시
# 조건 2. 출력 시 점수와 등급을 화면에 출력
# 조건 3. elif 문을 사용하여 프로그램 작성
# 사용자 입력 받은 숫자는 문자열형임
# 형 변환 : int(score)
score = input("점수를 입력하세요 : ")
score = int(score)
if score >= 95:
    print("점수 : {0}, 등급 : A+".format(score))
elif score >= 90:
    print("점수 : {0}, 등급 : A".format(score))
elif score >= 85:
    print("점수 : {0}, 등급 : B+".format(score))
elif score >= 80:
    print("점수 : {0}, 등급 : B".format(score))
elif score >= 75:
    print("점수 : {0}, 등급 : C+".format(score))
elif score >= 70:
    print("점수 : {0}, 등급 : C".format(score))
elif score >= 60:
    print("점수 : {0}, 등급 : D".format(score))
else:
    print("점수 : {0}, 등급 : F".format(score))