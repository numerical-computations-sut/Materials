"""Reference code for Homework 5, Question 7(a) (1400-2)."""

from __future__ import annotations

import math


def midpoint_rk2(f, x0, y0, x_end, h):
    """Integrate y'=f(x,y) with the explicit midpoint RK2 method."""
    if h <= 0 or x_end < x0:
        raise ValueError("Require h > 0 and x_end >= x0.")
    step_count = round((x_end - x0) / h)
    if not math.isclose(x0 + step_count * h, x_end, abs_tol=1e-12):
        raise ValueError("(x_end - x0) must be an integer multiple of h.")

    points = [(float(x0), float(y0))]
    x, y = points[0]
    for _ in range(step_count):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        x += h
        y += k2
        points.append((x, y))
    return points


def exact_solution(x):
    return 2 * math.exp(x) - x - 1


def main():
    x_end = float(input("x_end: "))
    h = float(input("h: "))
    points = midpoint_rk2(lambda x, y: x + y, 0.0, 1.0, x_end, h)
    approximation = points[-1][1]
    exact = exact_solution(x_end)
    print(f"RK2 approximation: {approximation:.12g}")
    print(f"Exact value:       {exact:.12g}")
    print(f"Absolute error:    {abs(approximation - exact):.6g}")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    xs, ys = zip(*points)
    dense_x = [x_end * i / 400 for i in range(401)]
    plt.plot(dense_x, [exact_solution(x) for x in dense_x], label="exact")
    plt.plot(xs, ys, "o--", label="midpoint RK2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
