# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# numbers에서 홀수 제거
# 홀수를 제거하려다 보니 리스트가 줄어들면서 리스트 전체를 확인하지 못하는 현상을 발견하였다.
# 그것을 방지하기 위해 2중 for문을 사용해야한다.
for i in range(len(numbers)):
    for j in numbers:
        if((j % 2) != 0):
            numbers.remove(j)

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)
