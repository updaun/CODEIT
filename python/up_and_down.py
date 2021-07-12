import random

question = random.randint(1,20)
count = 0

for i in range(4):
    number = int(input(f'기회가 {4-i}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: '))
    count += 1
    if number == question:
        print(f'축하합니다. {count}번만에 숫자를 맞히셨습니다.')
        break
    elif number > question:
        print("Down")
    elif number < question:
        print("Up")

if count == 4:
    print(f'. 정답은 {question}입니다.')
