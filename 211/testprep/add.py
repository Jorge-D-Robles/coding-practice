from fpdf import FPDF
import random
problems = []
tries = int(input("How many problems do you want?: "))

# This loop creates a dictionary with the problem and the answer. Problem = key, answer = value
for i in range(tries):
    a = random.randint(3, 9)
    b = random.randint(5, 20)
    problem = {f"{a} + {b}": a+b}
    # appends the dictionary to the empty list "problems"
    problems.append(problem)

i = 1  # counter variable for problem #
pdf = FPDF()  # creates a pdf object
pdf.add_page()  # adds a page to the pdf
pdf.set_font("Arial", size=15)  # sets the font and size

# loops through each problem added to the original list
for problem in problems:
    for key, value, in problem.items():
        # prints the problem and answer
        print(f"Problem # {i}: {key}")
        print(f"The answer is: {value}\n")

        # adds the problem and answer to the pdf, centered, same as print statements
        pdf.cell(200, 10, txt=f"Problem # {i}: {key}",
                 ln=2, align='C')
        pdf.cell(200, 10, txt=f"The answer is: {value}\n",
                 ln=2, align='C')
        i += 1  # increments the counter variable
# saves the pdf
pdf.output("add.pdf")
