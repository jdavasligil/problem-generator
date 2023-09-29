# problem-generator.py
# Jaedin Davasligil
# 29 September 2023
"""Generates LaTeX worksheet of random fraction addition problems.

This was created for Elementary SSAT Prep, and the script may be extended
in the future for more types of problems as a CLI tool.

Note: You need to use PDFLaTeX to generate the worksheet. I recommend Overleaf.
"""
import random as rnd

primes = [2,3,5,7]
author = "Jaedin Davasligil"
title = "Adding Fractions of Mixed Denominator"

def schrodinger():
    """It's both True and False until you measure it."""
    return bool(rnd.randint(0,1))

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

def write_document(writer):
    align_str_1 = " \\;\\; &= \\\\[.75in]\n"
    align_str_2 = " \\;\\; &= &\\\\[.75in]\n"
    problems_col_1 = []
    problems_col_2 = []

    for i in range(6):
        problems_col_1.append(generate_mixed_frac_sum(schrodinger()) + align_str_1)
        problems_col_2.append(generate_mixed_frac_sum(schrodinger()) + align_str_2)

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

if __name__ == "__main__":
    with open('worksheet.tex', 'w') as writer:
        write_document(writer)
