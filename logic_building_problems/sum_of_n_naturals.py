def sumOfNaturals (a: int):
    if (a ==1):
        return 1
    return a + sumOfNaturals(a - 1)

print(sumOfNaturals(3))
