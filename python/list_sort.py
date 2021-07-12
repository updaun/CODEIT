numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for i in range(0, len(numbers)):
    numbers.insert(i,numbers[-1])
    del numbers[-1]

print("뒤집어진 리스트: " + str(numbers))