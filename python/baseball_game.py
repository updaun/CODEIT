from random import randint

def generate_numbers():
    numbers = []
    while 2 >= len(numbers):
        random_number = randint(0,9)
        if random_number not in numbers:
            numbers.append(random_number)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

#print(generate_numbers())

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    i = 1
    while len(new_guess) <= 2:
        number = int(input(f'{i}번째 숫자를 입력하세요: '))
        if number <= 0 or number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        new_guess.append(number)
        i += 1

    return new_guess

def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in guess:
        if i in solution and guess.index(i) == solution.index(i):
            strike_count += 1
        if i in solution and guess.index(i) != solution.index(i):
            ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
#print(ANSWER)
tries = 0

while True:
    new_guess = take_guess()
    tries += 1
    s,b = get_score(new_guess, ANSWER)
    print(f'{s}S {b}B')
    if s == 3 and b == 0:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))