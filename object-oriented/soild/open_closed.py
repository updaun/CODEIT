# 개방 폐쇄 원칙 예제

from abc import ABC, abstractclassmethod

class Keyboard(ABC):
    """키보드 클래스"""
    @abstractclassmethod
    def save_input(self, content: str) -> None:
        """키보드 인풋 저장 메소드"""
        pass

    @abstractclassmethod
    def send_input(self) -> str:
        """키보드 인풋 전송 메소드"""
        pass
            
class AppleKeyboard(Keyboard):
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        #return self.keyboard.send_keyboard_input()

        # if isinstance(self.keyboard, AppleKeyboard):
        #     return self.keyboard.send_keyboard_input()
        # elif isinstance(self.keyboard, SamsungKeyboard):
        #     return self.keyboard.give_user_input()

        return self.keyboard.send_input()


class SamsungKeyboard(Keyboard):
    """삼성 키보드 클래스"""
    def __init__(self) -> None:
        self.user_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input
    
    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input


keyboard_manager = KeyboardManager()

apple_keyboard = AppleKeyboard()

samsung_keyboard = SamsungKeyboard()

keyboard_manager.connect_to_keyboard(apple_keyboard)

apple_keyboard.save_input("안녕하세요")

print(keyboard_manager.get_keyboard_input())

keyboard_manager.connect_to_keyboard(samsung_keyboard)

samsung_keyboard.save_input("안녕하세요")

print(keyboard_manager.get_keyboard_input())