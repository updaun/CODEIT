# 특수 메소드 __init__ 사용 예제

class User:
    # Magic method, special method, 특정 상황에서 자동으로 호출
    # 인스턴스가 생성될 때 자동으로 호출
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User('Young', 'young@codeit.kr', '123456')
#user1.initialize('Young', 'young@codeit.kr', '123456')

user2 = User('Yoonsoo', 'yoonsoo@codeit.kr', 'abcdef')
#user2.initialize('Yoonsoo', 'yoonsoo@codeit.kr', 'abcdef')

user3 = User('Lisa', 'lisa@codeit.kr', '123abc')
#user3.initialize('Lisa', 'lisa@codeit.kr', '123abc')

user4 = User('Young', 'young@codeit.kr', 'abc123')
#user4.initialize('Young', 'young@codeit.kr', 'abc123')

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)