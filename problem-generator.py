# problem-generator.py
# Jaedin Davasligil
# 29 September 2023
"""Generates LaTeX worksheet of random fraction addition problems.

This was created for Elementary SSAT Prep, and the script may be extended
in the future for more types of problems as a CLI tool.

Note: You need to use PDFLaTeX to generate the worksheet. I recommend Overleaf.
"""
import sys
import random as rnd

author = "Jaedin Davasligil"
title = "Adding Fractions of Mixed Denominator"

primes = [2,3,5,7]
problem_types = [
        "frac_sum",
        "frac_prod",
        ]

def schrodinger():
    """It's both True and False until you measure it."""
    return bool(rnd.randint(0,1))

def generate_mixed_frac_prod(easy=False):
    """Generates code for a mixed denominator fraction multiplication problem.

    Keyword arguments:
    easy -- whether or not the first denominator and second numerator cancel.
    """
    rnd.shuffle(primes)
    n1 = rnd.randint(1,7)
    d1 = rnd.randint(1,12)
    n2 = d1 if easy else rnd.randint(1,7)
    d2 = rnd.randint(1,12)
    frac_1 = "\\frac{" + str(n1) + "}{" + str(d1) + "}"
    frac_2 = "\\frac{" + str(n2) + "}{" + str(d2) + "}"
    sep = " \\;\\; \\times \\;\\; "

    return "\t\t" + frac_1 + sep + frac_2

def generate_mixed_frac_sum(easy=False):
    """Generates code for a mixed denominator fraction addition problem.

    Keyword arguments:
    easy -- whether or not the second denominator is a multiple of the first.
    """
    rnd.shuffle(primes)
    n1 = rnd.randint(1,6)
    d1 = primes[0]
    n2 = rnd.randint(1,6)
    d2 = rnd.randint(2,3) * d1 if easy else primes[1]
    frac_1 = "\\frac{" + str(n1) + "}{" + str(d1) + "}"
    frac_2 = "\\frac{" + str(n2) + "}{" + str(d2) + "}"
    sep = " \\;\\; + \\;\\; "

    return "\t\t" + frac_1 + sep + frac_2

def write_document(writer, problem_type):
    align_str_1 = " \\;\\; &= \\\\[.75in]\n"
    align_str_2 = " \\;\\; &= &\\\\[.75in]\n"
    problems_col_1 = []
    problems_col_2 = []
    problem_func = None

    match problem_type:

        case "frac_sum":
            problem_func = generate_mixed_frac_sum

        case "frac_prod":
            problem_func = generate_mixed_frac_prod

        case _:
            print("Error: problem_type invalid.")
            sys.exit()

    for i in range(6):
        problems_col_1.append(problem_func(schrodinger()) + align_str_1)
        problems_col_2.append(problem_func(schrodinger()) + align_str_2)

    header = [
            "\\documentclass{article}\n",
            "\\usepackage[margin=0.5in]{geometry}\n",
            "\\usepackage{fourier}\n",
            "\\usepackage{amsmath}\n",
            "\\usepackage{multicol}\n\n",
            "\\title{" + title + "}\n",
            "\\author{" + author + "}\n",
            "\\date{\\today}\n\n",
            ]
    top = [
            "\\begin{document}\n",
            "\\thispagestyle{empty}\n",
            "\\begin{center}\n",
           f"\\huge {title}\n",
            "\\end{center}\n",
            "\\begin{multicols}{2}\n",
            ]
    col_1 = [
            "\t\\vspace*{.5in} \\huge\n",
            "\t\\begin{align*}\n",
            ] + problems_col_1 + [
            "\t\\end{align*}\n\n",
            "\t\\columnbreak\n\n",
            ]
    col_2 = [
            "\t\\vspace*{.5in}\n",
            "\t\\begin{align*}\n",
            ] + problems_col_2 + [
            "\t\\end{align*}\n",
            ]
    bottom = [
            "\\end{multicols}\n",
            "\\end{document}",
            ]

    document = header + top + col_1 + col_2 + bottom

    writer.writelines(document)

def validate_args():
    if len(sys.argv) == 1:
        print("Error: No problem type specified.")
        sys.exit()

    problem_type = sys.argv[1]

    if not any(problem == problem_type for problem in problem_types):
        print("Error: Problem type is not valid.")
        sys.exit()

    return problem_type

if __name__ == "__main__":
    problem_type = validate_args()
    with open('worksheet.tex', 'w') as writer:
        write_document(writer, problem_type)
