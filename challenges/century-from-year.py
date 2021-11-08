import math

def centuryFromYear(year):
    century = year/100
    if century == math.floor(century):
        return int(century)

    return int(century + 1)

print(centuryFromYear(1701))