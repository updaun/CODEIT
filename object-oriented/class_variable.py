# 클래스 변수 사용 예제

class User:
    # 클래스 변수 선언
    count = 0
    # 유저 인스턴스의 모든 변수를 지정해주는 메소드
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        # 객체가 생성될 때마다 클래스 변수의 값을 1씩 증가
        User.count += 1

# User.count = 1
# print(User.count)

user1 = User('Young', 'young@codeit.kr', '123456')
user2 = User('Yoonsoo', 'yoonsoo@codeit.kr', 'abcdef')
user3 = User('Lisa', 'lisa@codeit.kr', '123abc')

# 같은 이름의 인스턴스 변수를 생성  ->  클래스 변수 우선순위 < 인스턴스 변수 우선순위
user1.count = 5

# 클래스 변수 설정
User.count = 5

print(User.count) 

print(user1.count)  
print(user2.count) 
print(user3.count) 
