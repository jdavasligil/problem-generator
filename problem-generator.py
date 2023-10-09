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
from itertools import chain

author = "Jaedin Davasligil"

# Add more primes for more variety and challenge.
primes = [2,3,5,7] 

# Key: Number used in problem generator.
# Val: Absolute frequency of that value occurring.
num_dist_map = {
        1:  1, 
        2:  3,
        3:  5,
        4:  5,
        5:  4,
        6:  4,
        7:  3,
        8:  3,
        9:  2,
        10: 1, 
        11: 1,
        12: 1,
        }
non_uniform_dist = sum([[k] for k,v in num_dist_map.items()], []) # Flatten
problem_types = [
        "frac_sum",
        "frac_prod",
        ]
type_titles = {
        problem_types[0]: "Adding Fractions of Mixed Denominator",
        problem_types[1]: "Multiplying Fractions",
        }

def schrodinger():
    """It's both True and False until you measure it."""
    return bool(rnd.randint(0,1))

def generate_mixed_frac_prod(easy=False):
    """Generates code for a mixed denominator fraction multiplication problem.

    Keyword arguments:
    easy -- whether or not the first denominator and second numerator cancel.
    """
    rnd.shuffle(primes)
    n1 = rnd.choice(non_uniform_dist)
    d1 = rnd.choice(non_uniform_dist)
    n2 = d1 if easy else rnd.choice(non_uniform_dist)
    d2 = rnd.choice(non_uniform_dist)
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
    """Given a problem type, writes a LaTeX document which produces a 12
       problem worksheet randomly according to the specified function.
    """
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

    title = type_titles[problem_type]

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
