from typing import List

class Friend:
    nicknames = [] # type: List

    def __init__(self, name: str) -> None:
        self.name = name

    def add_nickname(self, nickname: str) -> None:
        self.nicknames.append(nickname)

def main() -> List:
    Reemma = Friend("Reemma")
    Reemma.add_nickname("Rem")
    Reemma.add_nickname("Rema")
    return Reemma.nicknames

if __name__ == "__main__":
    res = main()
    print(res)