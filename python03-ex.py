#-*-coding:utf-8
# << 3장 연습문제 >>
print()
print("# if문 Q1.")
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

print()
print("# while문 Q1.")
i = 0
j = ''
while True:
    j += "*"
    i += 1
    if i > 5:
        break
    print(j)

print()
print("# while문 Q1-1.")
i = 0
while True:
    i += 1
    if i > 5:
        break
    print('*' * i)

print()
print("# for문 Q1.")
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for num in A:
    total += num
average = total / len(A)
print(average)