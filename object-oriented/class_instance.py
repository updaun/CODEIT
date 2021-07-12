# 클래스 안에 인스턴스 메소드 사용 예제

class User:
    # 인스턴스 메소드
    def say_hello(self):
        # 인사 메세지 출력 메소드
        print('안녕하세요! 저는 {}입니다.'.format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if(self.email == my_email and self.password == my_password):
            print('로그인 성공, 환영합니다.')
        else:
            print('로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.')
        
    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name
    
# 객체 생성
user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수 선언
user1.name = '김대위'
user1.email = 'captain@codeit.kr'
user1.password = '12345'

user2.name = '강영훈'
user2.email = 'younghoon@codeit.kr'
user2.password = '98765'

user3.name = '최지웅'
user3.email = 'jiwoong@codeit.kr'
user3.password = '78945'

# 출력
print(user1.email)
print(user2.password)

# 정의되지 않은 인스턴스 변수는 출력되지 않는다. (에러 발생)
# print(user1.age)

# 클래스 안에 있는 인스턴스 메소드 호출(객체 입력)
User.say_hello(user1)
# User.say_hello(user2)
# User.say_hello(user3)

# 인스턴스 메소드의 특별한 규칙 / 객체.인스턴스 메소드()
user1.say_hello() # = User.say_hello(user1)
# user1.say_hello(user1) # 오류 메세지 : TypeError: say_hello() takes 1 positional argument but 2 were given
# = User.say_hello(user1, user1) 객체를 두 번 입력하는 것과 같음 


#user1.login(user1, 'captain@codeit.kr', '12345') # 객체.인스턴스메소드()는 첫번째 인자로 객체가 자동으로 들어가기 때문에 잘못됨
user1.login('captain@codeit.kr', '12345')

# user1.name과 입력값이 같은지 확인하는 메소드
print(user1.check_name('김대위'))
print(user1.check_name('강영훈'))