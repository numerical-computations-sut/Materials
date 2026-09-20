import pandas as pd
import openpyxl
from math import isclose
from pathlib import Path


def y_prime(x, y):
    return 2 * x * y


def grid_points(b, h):
    if h <= 0 or b < 1:
        raise ValueError('Require h > 0 and b >= 1.')
    step_count = round((b - 1) / h)
    if not isclose(1 + step_count * h, b, rel_tol=0, abs_tol=1e-12):
        raise ValueError('(b - 1) must be an integer multiple of h.')
    return [1 + i * h for i in range(step_count + 1)]


def euler(b, h):
    euler_arr = [(1, 1)]
    for x_next in grid_points(b, h)[1:]:
        xi = euler_arr[-1][0]
        yi = euler_arr[-1][1]
        dt = x_next - xi
        y_next = yi + dt * y_prime(xi, yi)
        euler_arr.append((x_next, y_next))
    return euler_arr


def modified_euler(b, h):
    m_euler_arr = [(1, 1)]
    for x_next in grid_points(b, h)[1:]:
        xi = m_euler_arr[-1][0]
        yi = m_euler_arr[-1][1]
        dt = x_next - xi
        y_next_star = yi + dt * y_prime(xi, yi)
        y_next_prime_star = y_prime(x_next, y_next_star)
        y_next = yi + dt * (y_prime(xi, yi) + y_next_prime_star) / 2
        m_euler_arr.append((x_next, y_next))
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

data_path = Path(__file__).with_name('data.xlsx')
df = pd.read_excel(data_path)
df = df.loc[:, ~df.columns.astype(str).str.startswith('Unnamed:')]
if len(df) != len(e):
    raise ValueError('data.xlsx must have one row for every grid point.')
if 'x_n' not in df.columns or any(
    not isclose(float(stored), computed, rel_tol=0, abs_tol=1e-12)
    for stored, (computed, _) in zip(df['x_n'], e)
):
    raise ValueError('The x_n column in data.xlsx must match the requested grid.')
df.loc[:, 'Euler'] = [value for _, value in e]
df.loc[:, 'Modified Euler'] = [value for _, value in m_e]
df.to_excel(data_path, index=False)
