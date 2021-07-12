# 추상화의 좋은 예시

class BankAccount:
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, owner_name, balance):
        """인스턴스 변수 : name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance += amount

    def wirhdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1+ BankAccount.interest

# 어디에 쓰는 클래스이고 어떻게 사용할지 직관적으로 알 수 있다.
example_account = BankAccount("Hong Gil Dong", 1000)

# example_account.add_interest()
# print(example_account.balance)

# example_account.deposit(500)
# print(example_account.balance)

# example_account.wirhdraw(2000)
# example_account.wirhdraw(1000)
# print(example_account.balance)

# 클래스에 있는 docstring을 출력하는 메소드
# help(BankAccount) 

help(list)