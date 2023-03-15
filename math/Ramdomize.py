import sympy as sp
from sympy import symbols
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Configure matplotlib to use LaTeX
plt.rcParams["text.usetex"] = True


def save_random_points_slope_to_pdf(x1, y1, x2, y2, slope, file_name):
    fig, ax = plt.subplots()

    # Set the title
    ax.set_title("Random Points Slope Problem")

    # Display the points and slope as equations
    ax.text(0.5, 0.6, "Point 1: ({}, {})".format(x1, y1), fontsize=12,
            ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.5, "Point 2: ({}, {})".format(x2, y2), fontsize=12,
            ha='center', va='center', transform=ax.transAxes)
    ax.text(0.5, 0.4, r"$m = \frac{" + str(y2 - y1) + "}{" + str(x2 - x1) + "}$",
            fontsize=12, ha='center', va='center', transform=ax.transAxes)

    # Hide the axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Save the figure to a PDF
    with PdfPages(file_name) as pdf:
        pdf.savefig(fig, bbox_inches='tight')

    plt.close(fig)


x1, x2, y1, y2 = symbols('x1 x2 y1 y2')

x1 = sp.sympify(randint(-10, 10))
x2 = sp.sympify(randint(-10, 10))
y1 = sp.sympify(randint(-10, 10))
y2 = sp.sympify(randint(-10, 10))

m = (y2 - y1)/(x2 - x1)

# Save the random points and slope to a PDF
file_name = "randomizepointslope.pdf"
save_random_points_slope_to_pdf(x1, y1, x2, y2, m, file_name)
