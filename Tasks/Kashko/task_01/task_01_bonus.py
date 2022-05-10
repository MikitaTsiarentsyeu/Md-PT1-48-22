'''Finds roots of cubic equation (ax^3 + bx^2 + cx + d = 0).
Some problems with accuracy. It will be better to use Decimal
(or Fractions?) objects.
To fix...

'''

import math
import re


def get_user_input() -> tuple:

    # Regexp for matching integers.
    r = re.compile(r'^-?\d{0,}$')

    while True:
        a = str.strip(input('Enter "a" (integer)\n'))
        if re.match(r, a) is None:
            print('Enter integer, please!')
            continue
        a = int(a)
        break

    while True:
        b = str.strip(input('Enter "b" (integer)\n'))
        if re.match(r, b) is None:
            print('Enter integer, please!')
            continue
        b = int(b)
        break

    while True:
        c = str.strip(input('Enter "c" (integer)\n'))
        if re.match(r, c) is None:
            print('Enter integer, please!')
            continue
        c = int(c)
        break

    while True:
        d = str.strip(input('Enter "d" (integer)\n'))
        if re.match(r, d) is None:
            print('Enter integer, please!')
            continue
        d = int(d)
        break

    return (a, b, c, d)


def find_roots(coeffs: tuple) -> tuple:

    a = coeffs[1] / coeffs[0]
    b = coeffs[2] / coeffs[0]
    c = coeffs[3] / coeffs[0]

    q = (3 * b - a**2) / 9
    r = (9 * a * b - 2 * a**3 - 27 * c) / 54
    s = q**3 + r**2

    if s < 0:
        phi = (1 / 3) * math.acos(r / math.sqrt(-q**3))
        x1 = 2 * math.sqrt(-q) * math.cos(phi) - a / 3
        x2 = 2 * math.sqrt(-q) * math.cos(phi + 2 * math.pi / 3) - a / 3
        x3 = 2 * math.sqrt(-q) * math.cos(phi - 2 * math.pi / 3) - a / 3

    if s > 0:
        if q > 0:
            phi = (1 / 3) * math.acosh(abs(r) / math.sqrt(q**3))
            x1 = -2 * math.copysign(1,
                                    r) * math.sqrt(q) * math.cosh(phi) - a / 3
            x2 = complex(
                math.copysign(1, r) * math.sqrt(q) * math.cosh(phi) - a / 3,
                math.sqrt(3 * q) * math.sinh(phi))
            x3 = complex(
                math.copysign(1, r) * math.sqrt(q) * math.cosh(phi) - a / 3,
                -math.sqrt(3 * q) * math.sinh(phi))
        if q < 0:
            phi = (1 / 3) * math.asinh(abs(r) / math.sqrt(abs(q)**3))
            x1 = -2 * math.copysign(1, r) * math.sqrt(
                abs(q)) * math.sinh(phi) - a / 3
            x2 = complex(
                math.copysign(1, r) * math.sqrt(abs(q)) * math.sinh(phi) -
                a / 3,
                math.sqrt(3 * abs(q)) * math.cosh(phi))
            x3 = complex(
                math.copysign(1, r) * math.sqrt(abs(q)) * math.sinh(phi) -
                a / 3, -math.sqrt(3 * abs(q)) * math.cosh(phi))
        if q == 0:
            x1 = -(c - a**3 / 27)**(1 / 3) - a / 3
            x2 = complex(
                (-a + x1) / 2,
                math.sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b)) * 1 / 2)
            x3 = complex(
                (-a + x1) / 2,
                math.sqrt(abs((a - 3 * x1) * (a + x1) - 4 * b)) * -1 / 2)

    if s == 0:
        x1 = -2 * r**(1 / 3) - a / 3
        x2 = x3 = r**(1 / 3) - a / 3
    return (x1, x2, x3)


data = get_user_input()
roots = find_roots(data)
print(roots)
