# Find the equation of a line given two points (INPUT) - Output to PDF

from sympy import symbols, sympify, Eq, factor
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x, y, x1, x2, y1, y2, m = symbols('x y x1 x2 y1 y2 m')

x1 = sympify(input('Enter the x1 coordinate: '))
y1 = sympify(input('Enter the y1 coordinate: '))
x2 = sympify(input('Enter the x2 coordiante: '))
y2 = sympify(input('Enter the y2 coordinate: '))

m = (y2 - y1)/(x2 - x1)

line = m*x - m*x1 + y1

# point-slope form
left = y - y1
right = m*(x-x1)

# slope-intercept form
line = m*x - m*x1 + y1

# y-intercept
b = -m*x1 + y1

# x-intercept
x_int = -b/m

fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')

ax.text(0.5, 0.8, f"Given points: (${sp.latex(x1)}, {sp.latex(y1)})$, $({sp.latex(x2)}, {sp.latex(y2)})$",
        fontsize=16, ha='center', va='center')

ax.text(0.5, 0.7,
        f"Point-slope form of the line: ${sp.latex(Eq(left, factor(right)))}$", fontsize=16, ha='center', va='center')

ax.text(0.5, 0.6,
        f"Slope-intercept form of the line: ${sp.latex(Eq(y, line))}$", fontsize=16, ha='center', va='center')

ax.text(0.5, 0.5,
        f"X-intercept of the line: $({sp.latex(x_int)}, 0)$", fontsize=16, ha='center', va='center')

ax.text(0.5, 0.4,
        f"Y-intercept of the line: $(0, {sp.latex(b)})$", fontsize=16, ha='center', va='center')

with PdfPages('line_equation_given_two_points_output.pdf') as pdf:
    pdf.savefig(fig)
    plt.close()
