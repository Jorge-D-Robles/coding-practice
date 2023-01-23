'''
Find the point-slope and slope-intercept form PERPENDICULAR given a point and the
slope of a standard form of a line. (RANDOMIZE)
'''

from sympy import symbols, sympify, Eq
from random import randint

a, b, x, y, x1, y1 = symbols('a b x y x1 y1')

a = sympify(randint(1, 10))
b = sympify(randint(-10, 10))
x1 = sympify(randint(-10, 10))
y1 = sympify(randint(-10, 10))

# slope
m = -b/a

# Perpendicular slope
m_perp = 1/m

# point-slope form
left = y - y1
right = (m_perp)*(x-x1)

# slope-intercept form
line = (m_perp)*x - (m_perp)*x1 + y1

print('The coefficients of the standard form of a line are: ')
display((a, b))

print('The coordinates are: ')
display((x1, y1))

print('The slope is: ')
display(m)

print('The negative reciprocal slope is: ')
display(m_perp)

print('This is the point-slope form of the line: ')
display(Eq(left, right))

print('This is the slope-intercept form of the line: ')
display(Eq(y, line))
