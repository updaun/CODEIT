import random

def generate_number(n):
    result = []
    while n-1 >= len(result):
        number = random.randint(1,45)
        if number not in result:
            result.append(number)
    return result

def draw_winning_numbers():
    result = generate_number(7)
    return sorted(result[:6]) + result[-1:]

def count_matching_numbers(list1, list2):
    count = 0
    bonus_count = 0
    for i in list1:
        if i in list2[:6]:
            count += 1
        elif i == list2[-1]:
            bonus_count += 1
    return count, bonus_count

def check(list1,list2):
    result = ""
    match_count = count_matching_numbers(list1,list2)[0]
    bonus_match_count = count_matching_numbers(list1,list2)[1]
    
    if match_count == 3:
        result = "5,000원"
    elif match_count == 4:
        result = "50,000원"
    elif match_count == 5 and bonus_match_count == 0:
        result = "1,000,000원"
    elif match_count == 5 and bonus_match_count == 1:
        result = "50,000,000원"
    elif match_count == 6:
        result = "1,000,000,000원"
    else:
        result = "아쉽게도 당첨되지 않았습니다."

    return result

numbers_test = [2, 4, 11, 14, 25, 40]
winning_numbers_test = [4, 12, 14, 28, 40, 41, 6]

print(check(numbers_test, winning_numbers_test))

print(draw_winning_numbers())