from typing import List

class Friend:
    nicknames = [] # type: List

    def __init__(self, name: str) -> None:
        self.name = name
        self.previous_addresses : List = [] # only store the most recent 3 addresses

    def add_nickname(self, nickname: str) -> None:
        self.nicknames.append(nickname);

    def celebrate_birthday(self) -> None:
        self.age += 1

    def add_address(self, address: tuple) -> List[int]:
        if len(self.previous_addresses) > 2:
            self.previous_addresses = self.previous_addresses[-2:]
        self.previous_addresses.append(address)
        return [len(self.previous_addresses)]

def main() -> Friend:
    Reemma = Friend("Reemma")
    Reemma.add_nickname("Rem")
    Reemma.add_nickname("Rema")
    Reemma.celebrate_birthday()
    Reemma.previous_addresses = [(2.2, 37.4), (34.66, 856.2), (33.1, 12.0)]
    Reemma.add_address((12.3, 90.4))
    return Reemma

if __name__ == "__main__":
    res = main()
    print(res)