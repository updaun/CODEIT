class Empolyee:
    """직원 클래스"""
    company_name = "코드잇 버거" # 가게 이름
    raise_percentage = 1.03 # 시급 인상률

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def __str__(self):
        return Empolyee.company_name + " 직원: " + self.name


class Cashier(Empolyee):
    """계산대 직원 클래스"""
    # 변수 오버라이딩
    raise_percentage = 1.05
    
    burger_price = 4000 # 햄버거 가격
    # 오버라이딩
    def __init__(self, name, wage, number_sold=0):
        # self.name = name
        # self.wage = wage

        # Empolyee.__init__(self, name, wage)
        super().__init__(name, wage)

        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print('돈이 충분하지 않습니다.')
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name

class DeliveryMan(Empolyee):
    """배달원 클래스"""


    # def __init__(self, name, wage, on_standby):

    #     self.on_standby = on_standby



    # def deliver(self, address):
    #     """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 성명 메세지를 출력한다"""
    #     if self.on_standby:
    #         print(address + '로 배달 나갑니다!')
    #         self.on_standby = False
    #     else:
    #         print("이미 배달하러 나갔습니다!")

    # def back(self):
    #     """배달원을 복귀 처리한다"""
    #     self.on_standby = True

    # def __str__(self) -> str:
    #     return DeliveryMan.company_name + " 배달원: " + self.name

# Cashier test        
jiwoong = Cashier("최지웅", 8900, 0)

# mro(Method Resolution Order : 메소드 검색 순서) test
print(Cashier.mro())
jiwoong.raise_pay()

# print(jiwoong.wage)
# print(jiwoong.take_order(7000))
# print(jiwoong.take_order(3000))
# print(jiwoong.burger_price)
# print(Cashier.burger_price)
# print(jiwoong.number_sold)
# print(jiwoong)

# # DeliveryMan test
# taeho = DeliveryMan("성태호", 7000, True)
# taeho.raise_pay()
# print(taeho.wage)
# taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
# taeho.deliver("서울시 코드잇로 51 최고 건물 402호")
# taeho.back()
# taeho.deliver("서울시 코드잇로 51 최고 건물 402호")
# print(taeho)

# inheritance test
# younghoon = Cashier("강영훈", 8900)
# younghoon.raise_pay()
# print(younghoon.wage)
# print(younghoon)

