import pandas as pd
import openpyxl


def y_prime(x, y):
    return 2 * x * y


def euler(b, h):
    euler_arr = [(1, 1)]
    i = 1 + h
    while i <= b + h:
        xi = euler_arr[-1][0]
        yi = euler_arr[-1][1]
        y_next = yi + h * y_prime(xi, yi)
        euler_arr.append((i, y_next))
        i += h
    return euler_arr


def modified_euler(b, h):
    m_euler_arr = [(1, 1)]
    i = 1 + h
    while i <= b + h:
        xi = m_euler_arr[-1][0]
        yi = m_euler_arr[-1][1]
        y_next_star = yi + h * y_prime(xi, yi)
        y_next_prime_star = y_prime(i, y_next_star)
        y_next = yi + h * (y_prime(xi, yi) + y_next_prime_star) / 2
        m_euler_arr.append((i, y_next))
        i += h
    return m_euler_arr


h = float(input())
a = float(input())
b = float(input())
e = euler(b, h)
m_e = modified_euler(b, h)
print('Euler:')
for i in e:
    if a <= i[0] <= b:
        print(i)
print('Modified Euler:')
for i in m_e:
    if a <= i[0] <= b:
        print(i)

df = pd.read_excel('data.xlsx')
for i in range(len(e)):
    df['Euler'][i] = e[i][1]
    df['Modified Euler'][i] = m_e[i][1]
df.to_excel('data.xlsx')
