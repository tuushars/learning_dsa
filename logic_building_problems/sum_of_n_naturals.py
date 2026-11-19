# def sumOfNaturals (a: int):
#     if (a ==1):
#         return 1
#     return a + sumOfNaturals(a - 1)

def sumOfNaturals (a: int):
    return a * (a + 1) //2

print(sumOfNaturals(10))
