#!/usr/bin/env python3
import sys

USAGE = """
 USAGE: {script} initial_sum  percent  fixed_period  set_period \n
 \tCalculate deposit yield. See script source for more details
 """
USAGE = USAGE.strip()

args_sys = sys.argv
print(args_sys)

if len(args_sys) != 5:
    exit(USAGE.format(script=args_sys[0]))

args_sys = args_sys[1:]

initial_sum, percent, fixed_period, set_period = map(float, args_sys)

def deposit(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield"""
    per = percent/100
    set_period = set_period/12
    growh_1 = (1 + per)  ( set_period/fixed_period)

    total = initial_sum * growh_1

    one_manth = 1/12
    growh_one_manth = (1 + per)  (one_manth / fixed_period)
    print(growh_one_manth* initial_sum)
    print("Sum", total)

deposit(initial_sum, percent, fixed_period, set_period)