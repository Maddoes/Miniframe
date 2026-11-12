import json
from enum import Enum, auto


class Letters(Enum):
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()


with open("num.xls", 'w') as f:
    f.write(" ")
num = int(input("Chose you're number"))
i = 0
while int(num) != 1:
    i += 1
    if num % 2 == 0:
        num = int(num//2)
        print("Even: //2")
        print(num)
        with open("num.xls", 'a') as f:
            f.write(f"\n{str(num)}")
        continue
    else:
        num = num * 3 + 1
        print("Odd: *3 + 1")
        print(num)
        with open("num.xls", 'a') as f:
            f.write(f"\n{str(num)}")
        continue
