# Problem Generator
A Python script that produces LaTeX code which creates a worksheet with random problems.

## Description
This script is a simple hack which allows me to make these randomly generated worksheets quickly, under the constraints I need. A proper solution might be a web application that allows me to specify the number of problems, constraints, etc. and compiles the resulting .tex document into a pdf.

## Requirements
* Python 3
* PDFLatex (or use an online compiler like Overleaf)

## Usage
Enter the following into your console:
```
python3 problem-generator.py [Problem Type]
```
where `[Problem Type]` is one of:
* frac_prod
* frac_sum

## Motivation
As a tutor, I often need to produce practice problem worksheets for my students. Online solutions do not allow the precise fine tuning I need. For example, if I have a student learning multiplication of fractions and I want them to be able to cancel common factors, I would like to ensure my algorithm will occasionally produce problems that can be solved this way.

## Future Work
I may turn this into a full web app.
