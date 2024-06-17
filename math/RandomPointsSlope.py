from sympy import sympify, symbols, Eq
from random import randint
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Configure matplotlib to use LaTeX
plt.rcParams["text.usetex"] = True


def draw_problem(ax, x1, y1, x2, y2, slope, x_position, y_position, problem_number):
    ax.text(x_position, y_position, "\\#{}: Point 1: ({}, {})".format(
        problem_number, x1, y1), fontsize=12)
    ax.text(x_position, y_position - 0.05,
            "Point 2: ({}, {})".format(x2, y2), fontsize=12)
    ax.text(x_position, y_position - 0.1,
            r"$m = \frac{" + str(y2 - y1) + "}{" + str(x2 - x1) + "}$", fontsize=12)


# Create a figure and axis for the PDF
fig, ax = plt.subplots(figsize=(8.5, 11))  # Letter size
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Hide the axis
ax.set_xticks([])
ax.set_yticks([])

# Set the title
ax.text(0.5, 0.95, "Random Points Slope Problems", fontsize=16,
        ha='center', va='center', transform=ax.transAxes)

x1, x2, y1, y2, m = symbols('x1 x2 y1 y2 m')

for i in range(10):
    x1 = sympify(randint(-10, 10))
    x2 = sympify(randint(-10, 10))
    y1 = sympify(randint(-10, 10))
    y2 = sympify(randint(-10, 10))

    slope = (y2 - y1) / (x2 - x1)

    # Calculate the position of the problem on the page
    y_position = 0.85 - (i // 2) * 0.15
    x_position = 0.05 if i % 2 == 0 else 0.5

    # Draw the problem at the calculated position with the problem number
    draw_problem(ax, x1, y1, x2, y2, slope, x_position, y_position, i+1)

# Save the figure to a PDF
file_name = "random_points_slope.pdf"
with PdfPages(file_name) as pdf:
    pdf.savefig(fig, bbox_inches='tight', pad_inches=0)

plt.close(fig)
