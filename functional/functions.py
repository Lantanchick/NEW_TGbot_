import random

class User:
    name: str = None
    age: int = None
    password: str = None

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def save_user_password(self, password: str) -> None:
        self.password = password

    def get_password(self) -> str:
        if self.password:
            return self.password

    def user_write(self):
        with open('users.txt', 'w') as f:
            f.write(f"Login: {self.name}, Age: {self.age}, Password: {self.get_password()}")


class Action:
    def get_random_number(self) -> str:
        return "+7-9"+str(random.randint(100000000, 999999999))

    def get_capit_str(self, text: str):
        return text.capitalize()
