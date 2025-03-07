def compound_interest(principal, rate, times_compounded_per_year, years):
    """
    Calculate the compound interest.
    
    Parameters entered:
    principal (float): The initial amount of money.
    rate (float): Annual interest rate as a decimal.
    times_compounded_per_year (int): Number of times interest is compounded per year.
    years (int): Time in years the money is invested for.
    
    Returns:
    float: The total amount after compound interest.
    """
    A = principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * years)
    return A

# Example usage
principal = float(input("Please enter the principle amount you wish to invest: "))  # Initial amount of money entry.
rate =  (float(input("Please enter the interest rate offered to you: ")))/100           # Annual interest rate offered eg 10%. The percentage can be enter as is, as it will automatically converts it from a fraction to a decimal number.
times_compounded_per_year = float(input("Please enter the the duration of time interest whether it be yearly,semi-annually or quaterly is compunded per year: ")) # Yearly would be 1, semi-anually would be 2 and quaterly would be 4.
years = float(input("Please enter the period of time(years) you wish to invest your money for: ")) # Time in years that the money will be invested for.

final_amount = compound_interest(principal, rate, times_compounded_per_year, years)
print(f"The total amount after {years} years with compound interest is: ${final_amount:.2f}") # the :.2f function forats the output to 2 decimal places.