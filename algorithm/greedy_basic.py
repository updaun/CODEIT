def min_coin_count(value, coin_list):
    coin_count = 0
    coin_list.sort(reverse=True)
    for i in coin_list:
        while value >= i:
            value -= i
            coin_count += 1
    return coin_count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))

def course_selection(course_list):
    course_list.sort(key=lambda x :(x[1], x[0]))
    time_table = []
    x_finish = None
    
    for i in course_list:
        if i == course_list[0]:
            x_finish = i[1]
            time_table.append(i)
        elif i[0] > x_finish:
            x_finish = i[1]
            time_table.append(i)
            
    return time_table

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

# 가장 먼저 시작하는 수업을 고른다.
# 겹치는 수업이 가장 적은 수업을 고른다.
# 가장 짧은 수업을 고른다.
# 가장 먼저 끝나는 수업을 고른다.