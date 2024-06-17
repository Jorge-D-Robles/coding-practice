import sympy as sp
from sympy import symbols
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Configure matplotlib to use LaTeX
plt.rcParams["text.usetex"] = True


def save_random_points_slope_to_pdf(points, slope, file_name):
    fig, ax = plt.subplots()

    # Set the title
    ax.set_title("4 Random Points Slope Problems with Same Slope")

    for i, point_set in enumerate(points, start=1):
        x1, y1, x2, y2 = point_set
        ax.text(0.5, 1 - (i * 0.15), "{}. Point 1: ({}, {})  Point 2: ({}, {})"
                .format(i, x1, y1, x2, y2),
                fontsize=12, ha='center', va='center', transform=ax.transAxes)

    ax.text(0.5, 0.1, r"Slope: $m = " + str(slope) + "$",
            fontsize=12, ha='center', va='center', transform=ax.transAxes)

    # Hide the axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Save the figure to a PDF
    with PdfPages(file_name) as pdf:
        pdf.savefig(fig, bbox_inches='tight')

    plt.close(fig)


x1, x2, y1, y2 = symbols('x1 x2 y1 y2')

m = sp.sympify(input('What is the slope of the line: '))
points = []

for _ in range(5):  # change this number to add more problems
    x1 = sp.sympify(randint(-10, 10))
    x2 = sp.sympify(randint(-10, 10))
    y1 = sp.sympify(randint(-10, 10))
    y2 = m*(x2-x1)+y1
    points.append((x1, y1, x2, y2))

# Save the random points and slope to a PDF
file_name = "random_points_slope_4_problems_same_slope.pdf"
save_random_points_slope_to_pdf(points, m, file_name)
