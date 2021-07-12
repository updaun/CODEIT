# 데코레이터 사용 예제

# 데코레이터 함수 선언
def add_print_to(original):
    def wrapper():
        print('함수 시작')
        original()
        print('함수 끝')
    return wrapper # 함수를 반환

# 꾸며주는 데코레이터 함수 연결
@add_print_to
def print_hello():
    print('안녕하세요!')

# add_print_to(print_hello) # 출력 없음
# add_print_to(print_hello)() # 출력 됨

# print_hello를 꾸며줌
# print_hello = add_print_to(print_hello)
print_hello()

