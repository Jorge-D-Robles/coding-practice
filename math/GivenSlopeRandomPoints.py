# Generate 5 sets of points with a given slope and random coordinates

import sympy as sp
from sympy import symbols
from random import randint
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Configure matplotlib to use LaTeX
plt.rcParams["text.usetex"] = True


def save_given_slope_random_points_to_pdf(coords, file_name):
    fig, ax = plt.subplots()

    # Set the title
    ax.set_title("5 Sets of Points with Given Slope and Random Coordinates")

    for i, (x1, y1, x2, y2, slope) in enumerate(coords, 1):
        ax.text(0.5, 1 - 0.17 * i, f"Set {i}: Point 1: ({x1}, {y1}), Point 2: ({x2}, {y2}), Slope: $m = {slope}$",
                fontsize=10, ha='center', va='center', transform=ax.transAxes)

    # Hide the axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Save the figure to a PDF
    with PdfPages(file_name) as pdf:
        pdf.savefig(fig, bbox_inches='tight')

    plt.close(fig)


x1, x2, y1, y2 = symbols('x1 x2 y1 y2')

m = sp.sympify(input('What is the slope of the line: '))

coords = []
for _ in range(5):
    x1 = sp.sympify(randint(-10, 10))
    y1 = sp.sympify(randint(-10, 10))
    y2 = sp.sympify(randint(-10, 10))

    x2 = (y2 - y1 + m * x1) / m
    coords.append((x1, y1, x2, y2, m))

# Save the given slope and random points to a PDF
file_name = "five_sets_given_slope_random_points.pdf"
save_given_slope_random_points_to_pdf(coords, file_name)
