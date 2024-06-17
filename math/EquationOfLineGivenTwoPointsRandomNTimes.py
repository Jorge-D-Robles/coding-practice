# Find the equation of a line given two points (RANDOMIZED, n times) - Output to PDF

from sympy import symbols, sympify, Eq, factor
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from random import randint

x, y, x1, x2, y1, y2, m = symbols('x y x1 x2 y1 y2 m')

num = int(input('How many problems of these do you want? '))

with PdfPages('randomized_line_equation_given_two_points_n_times_output.pdf') as pdf:
    for i in range(num):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')

        x1 = sympify(randint(-10, 10))
        y1 = sympify(randint(-10, 10))
        x2 = sympify(randint(-10, 10))
        y2 = sympify(randint(-10, 10))

        if x1 != x2:
            m = (y2 - y1)/(x2 - x1)
            line = m*x - m*x1 + y1
            left = y - y1
            right = m*(x-x1)
        else:
            while x1 == x2:
                x1 = sympify(randint(-10, 10))
                x2 = sympify(randint(-10, 10))
            m = (y2 - y1)/(x2 - x1)
            line = m*x - m*x1 + y1
            left = y - y1
            right = m*(x-x1)

        ax.text(0.5, 0.85, f"Exercise #{i+1}:",
                fontsize=16, ha='center', va='center')

        ax.text(
            0.5, 0.7, f"First set of coordinates: (${sp.latex(x1)}, {sp.latex(y1)})$", fontsize=16, ha='center', va='center')

        ax.text(
            0.5, 0.6, f"Second set of coordinates: (${sp.latex(x2)}, {sp.latex(y2)})$", fontsize=16, ha='center', va='center')

        ax.text(
            0.5, 0.45, f"Point-slope form of the line: ${sp.latex(Eq(left, factor(right)))}$", fontsize=16, ha='center', va='center')

        ax.text(
            0.5, 0.3, f"Slope-intercept form of the line: ${sp.latex(Eq(y, line))}$", fontsize=16, ha='center', va='center')

        pdf.savefig(fig)
        plt.close()
