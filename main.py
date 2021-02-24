from typing import List

class Friend:
    nicknames = [] # type: List
    age = 0 # type: int

    def __init__(self, name: str) -> None:
        self.name = name

    def add_nickname(self, nickname: str) -> None:
        self.nicknames.append(nickname)

    def celebrate_birthday(self) -> None:
        self.age += 1

def main() -> List:
    Reemma = Friend("Reemma")
    Reemma.add_nickname("Rem")
    Reemma.add_nickname("Rema")
    Reemma.celebrate_birthday()
    return Reemma.age

if __name__ == "__main__":
    res = main()
    print(res)