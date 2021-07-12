import random

with open("./codeit/vocabulary.txt", 'r', encoding='utf-8') as f:
    #line = f.readline()
    question_dict={}
    while True:
        line = f.readline().strip()
        data = line.split(": ")
        #print(data)
        if data == ['']:
            break
        question_dict[data[0]] = data[1]
    #print(list(question_dict.values()))

while True:
    random_question = random.choice(list(question_dict.values()))
    answer = input(f'{random_question}: ')
    answer_index = list(question_dict.values()).index(random_question)
    answer_check = list(question_dict.keys())[answer_index]
    if answer == 'q':
        break

    if answer == answer_check:
        print("맞았습니다!")
    else:
        print(f"아쉽습니다. 정답은 {answer_check}입니다.")

# 모범 답안

