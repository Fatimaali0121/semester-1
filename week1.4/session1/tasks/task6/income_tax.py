# Week 4, Session 1: Task 3

# You are given the function income_tax_calculator and a docstring.
# Your task is to write the body of the function based on the
# details in the docstring. You can create additional functions
# to be called from within income_tax_calculator


def income_tax_calculator(annual_income):
    """
    This function calculates the tax amount for a given taxable annual income
    based on the UK tax rates and allowances. The tax is calculated
    progressively across tax bands, as per the following rates and allowances:

    Band               |  Taxable income   | Tax rate
    Personal allowance | Up to 12,570      | 0%
    Basic rate         | 12,571 to 50,270  | 20%
    Higher rate        | 50,271 to 125,140 | 40%
    Additional rate    | over 125,140      | 45%

    Key Details:
    Personal Allowance: The first £12,570 of taxable income is tax-free.
    Progressive Taxation: Income tax is applied progressively across bands.
    For example, an annual income of £25,000 would be taxed as follows:
    The first £12,570 at 0% (personal allowance).
    The remaining £12,430 (i.e., £25,000 - £12,570) at 20% (basic rate).

    Args:
        annual_income: float

    Returns:
        a float, representing the total calculated tax, rounded to
        one decimal point. You can use the round() function,
        e.g round(tax, 1) 0.0 if annual_income is not a positive integer.
    """
    if type(annual_income) not in (float, int) or annual_income <=0:     # you can't use douple or on for int one for float because if it's not an a float num it's gonna be an int and the code gonna raise a true, so it will return 0.0
        return 0.0
    
    if annual_income < 12570:
        return 0.0

    tax = 0

# we used new if loops not if and elsif, because we want to calculate prograssive tax so we want the remiaing annual income to go through the rest of the if loops to calculate prograssive tax
# if it was not a prograssive tax we should've used if else, because in using if elsif the computer stop checking asa it finds one true condition. and we don't want that we want the same income go through all if loops to calc prograssive tax
    
    if annual_income > 125140:               
        tax += (annual_income - 125140) * 0.45
        annual_income = 125140              # remaining annual_income after calculating first patrt of prograssive tax, so we can apply rest of prograssive tax on it
                                          
    if annual_income > 50270:
        tax += (annual_income - 50270) * 0.40
        annual_income = 50270

    if annual_income > 12570:
        tax += (annual_income - 12570) * 0.20
        # no need to give remaining annual income a variable, as if it's less than 12570, it's tax free

    return round(tax, 1)

    
    
# Check if the following lines produce the correct output
print(income_tax_calculator(12000))     # 0.0
print(income_tax_calculator(14000))     # 286.0
print(income_tax_calculator(25000))     # 2486.0
print(income_tax_calculator(100000))    # 27432.0
print(income_tax_calculator(200000))
print(income_tax_calculator(-10000))
