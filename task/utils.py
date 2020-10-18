from math import *


def get_the_number(number):
    if sqrt(5 * number ** 2 + 4) % 1 == 0 or sqrt(5 * number ** 2 - 4) % 1 == 0:
        fibonancci_number = number
    else:
        c = 0
        while True:
            c += 1
            if sqrt(5 * (number + c) ** 2 + 4) % 1 == 0 or sqrt(5 * (number + c) ** 2 - 4) % 1 == 0:
                fibonancci_number = number + c
                break
            if sqrt(5 * (number - c) ** 2 + 4) % 1 == 0 or sqrt(5 * (number - c) ** 2 - 4) % 1 == 0:
                fibonancci_number = number - c
                break
    return fibonancci_number
