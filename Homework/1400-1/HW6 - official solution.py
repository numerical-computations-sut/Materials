"""Reference implementations for Homework 6, Question 6 (1400-1)."""

from __future__ import annotations

import math


def _matrix(a):
    rows = [list(map(float, row)) for row in a]
    if not rows or any(len(row) != len(rows) for row in rows):
        raise ValueError("A must be a nonempty square matrix.")
    return rows


def doolittle(a, tol=1e-12):
    """Return A=L@U with unit diagonal in L, without pivoting."""
    a = _matrix(a)
    n = len(a)
    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]
    for i in range(n):
        lower[i][i] = 1.0
        for j in range(i, n):
            upper[i][j] = a[i][j] - sum(lower[i][k] * upper[k][j] for k in range(i))
        if abs(upper[i][i]) <= tol and i < n - 1:
            raise ValueError("Doolittle encountered a zero pivot; pivoting is required.")
        for j in range(i + 1, n):
            lower[j][i] = (
                a[j][i] - sum(lower[j][k] * upper[k][i] for k in range(i))
            ) / upper[i][i]
    return lower, upper


def crout(a, tol=1e-12):
    """Return A=L@U with unit diagonal in U, without pivoting."""
    a = _matrix(a)
    n = len(a)
    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]
    for j in range(n):
        upper[j][j] = 1.0
        for i in range(j, n):
            lower[i][j] = a[i][j] - sum(lower[i][k] * upper[k][j] for k in range(j))
        if abs(lower[j][j]) <= tol and j < n - 1:
            raise ValueError("Crout encountered a zero pivot; pivoting is required.")
        if j < n - 1:
            for i in range(j + 1, n):
                upper[j][i] = (
                    a[j][i] - sum(lower[j][k] * upper[k][i] for k in range(j))
                ) / lower[j][j]
    return lower, upper


def cholesky(a, tol=1e-12):
    """Return lower-triangular L with A=L@L.T for symmetric positive-definite A."""
    a = _matrix(a)
    n = len(a)
    if any(abs(a[i][j] - a[j][i]) > tol for i in range(n) for j in range(n)):
        raise ValueError("Cholesky requires a symmetric matrix.")
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            residual = a[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if residual <= tol:
                    raise ValueError("Cholesky requires a positive-definite matrix.")
                lower[i][j] = math.sqrt(residual)
            else:
                lower[i][j] = residual / lower[j][j]
    return lower


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(column) for column in zip(*a)]


def _read_problem():
    n = int(input("Matrix dimension n: "))
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    print(f"Enter {n} rows, with {n} numbers in each row:")
    matrix = []
    for row_number in range(1, n + 1):
        row_text = input(f"row {row_number}: ").replace(",", " ")
        row = [float(value) for value in row_text.split()]
        if len(row) != n:
            raise ValueError(f"row {row_number} must contain exactly {n} numbers.")
        matrix.append(row)
    method = input("Method (Doolittle, Crout, or Cholesky): ").strip().lower()
    return matrix, method


def _print_matrix(name, matrix):
    print(f"{name} =")
    for row in matrix:
        print("  [" + "  ".join(f"{value:.12g}" for value in row) + "]")


def main():
    try:
        matrix, method = _read_problem()
        if method == "doolittle":
            lower, upper = doolittle(matrix)
            _print_matrix("L", lower)
            _print_matrix("U", upper)
        elif method == "crout":
            lower, upper = crout(matrix)
            _print_matrix("L", lower)
            _print_matrix("U", upper)
        elif method == "cholesky":
            lower = cholesky(matrix)
            _print_matrix("L", lower)
            _print_matrix("L.T", transpose(lower))
        else:
            raise ValueError("method must be Doolittle, Crout, or Cholesky.")
    except (EOFError, ValueError) as error:
        print(f"Decomposition is not possible: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
