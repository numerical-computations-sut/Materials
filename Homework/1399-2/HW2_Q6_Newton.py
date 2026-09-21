from math import *
import sys


f_string = input()
g_string = input()
n, x = map(float, input().split())

f = eval("lambda x: " + f_string)
g = eval("lambda x: " + g_string)

for i in range(int(n)):
    try:
        x = x - f(x) / g(x)
    except ZeroDivisionError:
        print("zero division")
        sys.exit()

print("answer:", "{:.5f}".format(x))
