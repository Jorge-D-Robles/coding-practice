import sympy as sp
from sympy import symbols, Eq, sin, cos, exp, ln, sqrt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from random import choice, randint
from func_timeout import func_timeout, FunctionTimedOut

x, C = symbols('x C')


def random_function():
    """
    Generate a random function with a combination of trigonometric,
    exponential, and logarithmic functions with random exponents.
    """
    random_exponent = randint(1, 3)
    base_functions = [
        randint(1, 5) * sin(x)**randint(1, 3),
        randint(1, 5) * cos(x)**randint(1, 3),
        randint(1, 5) * exp(x)**randint(1, 3),
        randint(1, 5) * ln(x)**randint(1, 2),
        randint(1, 5) * (1/x)**randint(1, 2),
        randint(1, 5) * sqrt(x)**randint(1, 2),
        randint(1, 5) * x**randint(1, 4)
    ]

    num_functions = randint(1, 4)
    if num_functions == 1:
        operation = choice(['+', '-', '*', '/'])
        if operation == '+':
            return (x**randint(0, 3) + choice(base_functions))
        elif operation == '-':
            return (x**randint(0, 3) - choice(base_functions))
        elif operation == '*':
            return (x**randint(0, 3) * choice(base_functions))
        elif operation == '/':
            return (x**randint(0, 3) / choice(base_functions))
    else:
        first_function = choice(base_functions)
        base_functions.remove(first_function)
        second_function = choice(base_functions)
        operation = choice(['+', '-', '*', '/'])

        if operation == '+':
            return (first_function + second_function)
        elif operation == '-':
            return (first_function - second_function)
        elif operation == '*':
            return first_function * second_function
        elif operation == '/':
            return (first_function / second_function)


num_problems = int(input('How many problems do you want? '))
problems_per_page = 5

# Create a PDF file to save the problems
with PdfPages('indefinite_integral_problems_solutions.pdf') as pdf:
    # Calculate the number of pages needed
    num_pages = (num_problems + problems_per_page - 1) // problems_per_page

    for page in range(num_pages):
        # Create a plot with a single column of subplots for each problem on the page
        num_problems_on_page = min(
            problems_per_page, num_problems - page * problems_per_page)
        fig, axs = plt.subplots(num_problems_on_page, 1, figsize=(11, 8.5))

        for i in range(num_problems_on_page):
            success = False
            while not success:
                # Choose a random function
                func = random_function()

                # Integrate the function with a timeout of 1 second
                try:
                    integral = func_timeout(1, sp.integrate, args=(func, x))
                    if not isinstance(integral, sp.Integral):
                        success = True
                except FunctionTimedOut:
                    pass

            # Generate the problem and solution
            problem = Eq(sp.Integral(func, x), integral + C)

            # Set plot parameters
            ax = axs[i] if num_problems_on_page > 1 else axs
            ax.axis('off')
            ax.text(0.5, 0.5, f"Ex {page * problems_per_page + i + 1}: ${sp.latex(problem)}$",
                    fontsize=12, ha='center', va='center')

        # Adjust the layout of subplots
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9,
                            bottom=0.1, hspace=0.5)

        # Save the plot to the PDF
        pdf.savefig(fig)
        plt.close()
