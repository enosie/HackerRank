import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    
    tip = meal_cost * tip_percent / 100
    percent = meal_cost * tax_percent / 100
    total = int(round(meal_cost + tip + percent))
    print(total) 

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)