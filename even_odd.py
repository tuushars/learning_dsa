# def isEven (n: int):
#     return (n % 2) == 0

def isEven (n: int):
    return (n & 1) == 0

print(isEven(10))