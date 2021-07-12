# 클래스 캡슐화 예제
# 1. 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단하는 것
# 2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것
# _(언더바) 로 캡슐화, 경고, 파이썬 개발자 사이에서의 문화

class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self._age = age
        # 나이 음수 방지를 위한 set_age 메소드 적용
        # self.set_age(age)
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age

    def __str__(self) -> str:
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + '씨는 ' + str(self._age) + '살입니다!'

    # getter method
    @property # 캡슐화를 위해 추가적인 소스 수정이 없다.
    def age(self):
        print('나이를 리턴합니다.')
        return self._age

    # setter method
    @age.setter
    def age(self, value):
        print('나이를 설정합니다.')
        if value < 0:
            print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
            self._age = 0
        else:
            self._age = value

    # __age 변수에 접근 가능한 메소드 getter 메소드
    # def get_age(self):
    #     """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 getter 메소드"""
    #     return self._age
    # __age 변수에 접근 가능한 메소드 setter 메소드
    # def set_age(self, value):
    #     """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 setter 메소드"""
        # self.__age = value
        # value에 음수가 들어오게 되면 나이가 음수가 되버리는 것을 방지 
        # if value < 0:
        #     print('나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.')
        #     self._age = 0
        # else:
        #     self._age = value

kyusik = Citizen('최규식', 25, "12345678")
young = Citizen('younghoon kang', -5, '87654321')

# 외부에서 접근 불가 (변수 및 인스턴스 메소드에 적용 가능)
# print(kyusik.__resident_id)
# print(kyusik.__age)
# kyusik.__authenticate("12345678")

# print(young.get_age())
# young.set_age(30)  
# print(young.get_age())

print(young.age) # @property = age.getter 메소드 사용 
young.age = 30 # age.setter 메소드 사용되며 30을 value로 입력
print(young.age)

