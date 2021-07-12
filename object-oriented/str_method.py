# 특수 메소드 __str__ 사용 예제

class User:
    # 유저 인스턴스의 모든 변수를 지정해주는 메소드
    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print('안녕하세요! 저는 {}입니다.'.format(self.name))

    # 특수 메소드, double underscore -> dunder method
    # 특정 상황에서 자동으로 호출 (print 함수를 호출할 때)
    def __str__(self) -> str:
        return "사용자 : {}, 이메일 : {}, 비밀번호 : ******".format(self.name, self.email)

user1 = User('Young', 'young@codeit.kr', '123456')
user2 = User('Yoonsoo', 'yoonsoo@codeit.kr', 'abcdef')

print(user1) # __str__ 메소드 사용 전 <__main__.User object at 0x000001D61AC2AE88>
print(user2) # __str__ 메소드 사용 전 <__main__.User object at 0x000001D61AC2AF48>