# Find the equation of a line given two points (RANDOMIZED) - Output to PDF

from sympy import symbols, sympify, Eq
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from random import randint

x, y, x1, x2, y1, y2, m = symbols('x y x1 x2 y1 y2 m')

x1 = sympify(randint(-10, 10))
y1 = sympify(randint(-10, 10))
x2 = sympify(randint(-10, 10))
y2 = sympify(randint(-10, 10))

if x1 != x2:
    m = (y2 - y1)/(x2 - x1)
    line = m*x - m*x1 + y1
else:
    while x1 == x2:
        x1 = sympify(randint(-10, 10))
        x2 = sympify(randint(-10, 10))
    m = (y2 - y1)/(x2 - x1)
    line = m*x - m*x1 + y1

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

ax.text(0.5, 0.8,
        f"First set of coordinates: (${sp.latex(x1)}, {sp.latex(y1)})$", fontsize=16, ha='center', va='center')

ax.text(0.5, 0.6,
        f"Second set of coordinates: (${sp.latex(x2)}, {sp.latex(y2)})$", fontsize=16, ha='center', va='center')

ax.text(0.5, 0.4,
        f"Slope-intercept form of the line: ${sp.latex(Eq(y, line))}$", fontsize=16, ha='center', va='center')

with PdfPages('randomized_line_equation_given_two_points_output.pdf') as pdf:
    pdf.savefig(fig)
    plt.close()
