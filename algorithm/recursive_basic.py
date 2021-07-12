# 재귀 함수 연습

def factorial(n):
    if n == 0:
        return 1

    return factorial(n - 1) * n

print(factorial(2000))

def fib(n):
    # base case
    if n < 3:
        return 1
    
    # recursive case
    return fib(n - 1) + fib(n - 2)
    
# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))


def triangle_number(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))


def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)

print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    string = str(n)
    if len(string) == 1:
        return int(n)
    return int(string[0]) + sum_digits(string[1:])

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    global new_list 
    if len(some_list) == 1:
        new_list.append(some_list[0])
        return new_list
    new_list.append(some_list.pop())
        
        
    return flip(some_list)

new_list = []
# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # base case
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    # recursive case
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # start_index가 end_index보다 크면 some_list안에 element는 없다
    if start_index > end_index:
        return None
      
    # 범위의 중간 인덱스를 찾는다
    mid = (start_index + end_index) // 2
  
    # 이 인덱스의 값이 찾는 값인지 확인을 해준다
    if some_list[mid] == element:
        return mid

    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색해준다
    if element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)

    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색해준다
    else:
        return binary_search(element, some_list, mid + 1, end_index)        

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))


def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    binary = (start_index + end_index)//2
    if binary == 0:
        if element != some_list[0]:
            return None
    elif binary == end_index:
        if element != some_list[end_index]:
            return None
    
    if element < some_list[binary]:
        return binary_search(element, some_list[:binary], end_index = binary)
    elif element > some_list[binary]:
        return binary_search(element, some_list[binary:], start_index = binary)
    elif element == some_list[binary]:
        return binary + start_index

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))



## 하노이의 탑
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # base case: 옮길 원판이 없으면 부분 문제를 나누지 않고 함수를 끝낸다
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        
        # 1. 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
        hanoi(num_disks - 1, start_peg, other_peg)
        
        # 2. 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)
        
        # 3. 나머지 원판들을 other_peg에서 end_peg로 이동
        hanoi(num_disks - 1, other_peg, end_peg)

# 테스트
hanoi(3, 1, 3)