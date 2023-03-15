# Factoring Quadratics and Output to PDF - Continuous Input - Single Page

from sympy import sympify, symbols, Symbol, factor, Eq
from random import randint
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from IPython.display import display

x, a, b, c = symbols('x a b c')

def input_coefficient(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'stop':
            return None
        try:
            return sympify(user_input)
        except:
            print("Invalid input. Please try again or type 'stop' to exit.")

fig, ax = plt.subplots(figsize=(6, 9))
ax.axis('off')

with PdfPages('factoring_quadratics_output_single_page.pdf') as pdf:
    current_y = 0.9
    while True:
        print("Type 'stop' to exit the script.")
        a = input_coefficient('Enter the coefficient for x-squared term: ')
        if a is None:
            break
        b = input_coefficient('Enter the coefficient for x term: ')
        if b is None:
            break
        c = input_coefficient('Enter the coefficient for the constant term: ')
        if c is None:
            break

        quad = a*x**2 + b*x + c
        factored_quad = factor(quad)

        # Display the equation in the console
        display(Eq(quad, factored_quad))

        # Output to PDF
        eq_str = f"${sp.latex(Eq(quad, 0))} \\Rightarrow {sp.latex(Eq(factored_quad, 0))}$"
        ax.text(0.5, current_y, eq_str, fontsize=16, ha='center', va='center')
        current_y -= 0.1

    pdf.savefig(fig)
    plt.close()
