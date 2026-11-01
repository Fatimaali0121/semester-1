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

    no_tax = 12570
    progressive_tax1 = 50270
    progressive_tax2 = 125140


    if annual_income <= 12570:
        return 0
    
    elif annual_income <= 50270:
        taxable_income = annual_income - no_tax 
        tax = taxable_income * 0.20
        return round(tax, 1)
    
    elif annual_income <= 125140:
        taxable_income1 = annual_income - no_tax
        tax1 = taxable_income1 * 0.20
        taxable_income2 = taxable_income1 - progressive_tax1
        tax2 = taxable_income2 * 0.40
        tax = tax1 + tax2
        return round(tax,1)
    
    else:
        taxable_income = annual_income - no_tax
        tax1 = taxable_income1 * 0.20
        taxable_income2 = taxable_income1 - progressive_tax1
        tax2 = taxable_income2 * 0.40
        taxable_income3 = taxable_income2 - progressive_tax2
        tax3 = taxable_income3 * 0.45
        tax = tax1 + tax2 + tax3
        return round(tax, 1)



# Check if the following lines produce the correct output
print(income_tax_calculator(12000))     # 0.0
print(income_tax_calculator(14000))     # 286.0
print(income_tax_calculator(25000))     # 2486.0
print(income_tax_calculator(100000))    # 27432.0
