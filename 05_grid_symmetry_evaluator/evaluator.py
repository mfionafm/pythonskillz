from math import gcd
from collections import Counter


def get_partitions(n, i=1):
    yield [n]
    for x in range(i, n // 2 + 1):
        for p in get_partitions(n - x, x):
            yield [x] + p


def factorial_table_upto(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i
    return fact


def conjugacy_class_size(partition, n, fact):
    """
    |S_n| / z_lambda where z_lambda = ∏ k^m_k m_k!
    """
    counts = Counter(partition)

    denom = 1
    for k, m in counts.items():
        denom *= (k ** m) * fact[m]

    return fact[n] // denom


def orbit_exponent(row_cycles, col_cycles):
    """
    Exact cycle-index evaluation of the product action:
    each (r, c) contributes gcd(r, c)
    """
    total = 0
    for r in row_cycles:
        for c in col_cycles:
            total += gcd(r, c)
    return total


def solution(w, h, s):
    fact = factorial_table_upto(max(w, h))

    total = 0

    for row_part in get_partitions(h):
        row_weight = conjugacy_class_size(row_part, h, fact)

        for col_part in get_partitions(w):
            col_weight = conjugacy_class_size(col_part, w, fact)

            exp = orbit_exponent(row_part, col_part)

            total += row_weight * col_weight * (s ** exp)

    return str(total // (fact[w] * fact[h]))


print(solution(2, 2, 2))  # "7"
