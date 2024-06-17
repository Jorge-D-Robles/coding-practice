# Find the point-slope and slope-intercept form given a point and the
# slope of a standard form of a line. (INPUT) - Output to PDF

from sympy import symbols, sympify, Eq
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

a, b, x, y, x1, y1 = symbols('a b x y x1 y1')

a = sympify(input('Enter the coefficient of x: '))
b = sympify(input('Enter the coefficient of y: '))
x1 = sympify(input('Enter the x-coordinate: '))
y1 = sympify(input('Enter the y-coordinate: '))

# slope
m = -a/b

# point-slope form
left = y - y1
right = m*(x-x1)

# slope-intercept form
line = m*x - m*x1 + y1

with PdfPages('line_given_point_slope_input_output.pdf') as pdf:
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')

    ax.text(
        0.5, 0.7, f"Point-slope form of the line: ${sp.latex(Eq(left, right))}$", fontsize=16, ha='center', va='center')

    ax.text(
        0.5, 0.4, f"Slope-intercept form of the line: ${sp.latex(Eq(y, line))}$", fontsize=16, ha='center', va='center')

    pdf.savefig(fig)
    plt.close()
