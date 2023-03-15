# Generate a point with a given slope and input coordinates

import sympy as sp
from sympy import symbols
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Configure matplotlib to use LaTeX
plt.rcParams["text.usetex"] = True

def save_given_points_slope_to_pdf(x1, y1, x2, y2, slope, file_name):
    fig, ax = plt.subplots()

    # Set the title
    ax.set_title("Point with Given Slope and Input Coordinates")

    ax.text(0.5, 0.7, "Point 1: ({}, {})".format(x1, y1),
            fontsize=12, ha='center', va='center', transform=ax.transAxes)

    ax.text(0.5, 0.5, "Point 2: ({}, {})".format(x2, y2),
            fontsize=12, ha='center', va='center', transform=ax.transAxes)

    ax.text(0.5, 0.3, r"Slope: $m = " + str(slope) + "$",
            fontsize=12, ha='center', va='center', transform=ax.transAxes)

    # Hide the axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Save the figure to a PDF
    with PdfPages(file_name) as pdf:
        pdf.savefig(fig, bbox_inches='tight')

    plt.close(fig)

x1, x2, y1, y2 = symbols('x1 x2 y1 y2')

x1 = sp.sympify(input('Type the x1 coordinate: '))
y1 = sp.sympify(input('Type the y1 coordinate: '))
x2 = sp.sympify(input('Type the x2 coordinate: '))
m = sp.sympify(input('What is the slope of the line: '))
y2 = m*(x2-x1)+y1

# Save the given points and slope to a PDF
file_name = "given_points_slope.pdf"
save_given_points_slope_to_pdf(x1, y1, x2, y2, m, file_name)
