# 클래스 메소드 사용 예제

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

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print('안녕하세요! 저는 {}입니다.'.format(self.name))

    # 특수 메소드, double underscore -> dunder method
    # 특정 상황에서 자동으로 호출 (print 함수를 호출할 때)
    def __str__(self):
        return "사용자 : {}, 이메일 : {}, 비밀번호 : ******".format(self.name, self.email)

    # 클래스 메소드 생성, 첫 번째 파라미터로 클래스가 자동 전달 
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는 : {}입니다".format(cls.count)) # User.count와 같다.

    # 클래스 메소드에서 인스턴스 메소드로 변경
    # 처음에 인스턴스 메소드로 하지 않고 클래스 메소드로 한 이유는 인스턴스 변수가 없기 때문이다.
    # 클래스 메소드는 인스턴스 변수를 사용할 수 없다!
    # 인스턴스가 하나도 없더라도 필요한 변수가 존재하기 때문에 클래스 메소드를 사용한다.
    # def number_of_users(self):
    #     print("총 유저 수는 : {}입니다".format(User.count)) # User.count와 같다.

# user1 = User("Young", "young@codeit.kr", "123456")
# user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
# user3 = User("Taeho", "taeho@codeit.kr", "123abc")

# 클래스 메소드 호출
# 인스턴스가 1개도 없을 때 호출 (총 유저 수는 : 0입니다)
User.number_of_users() 
# user1.number_of_users()

# 클래스 메소드에서 인스턴스 메소드로 변경 후 호출 
# User.number_of_users(user1)
# user1.number_of_users()