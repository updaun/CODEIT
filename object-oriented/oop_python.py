# 파이썬은 순수 객체 지향 언어

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))
    

user1 = User("Young", "young@codeit.kr", "123456")

print(type(user1)) # 객체 <class '__main__.User'>

print(type(2)) # 숫자 <class 'int'>
print(type("string")) # 문자 <class 'str'>
print(type([])) # 리스트 <class 'list'>
print(type({})) # 딕셔너리 <class 'dict'>
print(type(())) # 튜플 <class 'tuple'>

def print_hello():
    print("안녕하세요")

print(type(print_hello)) # 함수 <class 'function'>

# 1 # 숫자 클래스로 만든 1

# "" # 문자열 클래스로 만든 빈 문자열

# 만들어진 메소드를 활용

int_list = []

int_list.append(1)
int_list.append(3)
int_list.append(7)

print(int_list)