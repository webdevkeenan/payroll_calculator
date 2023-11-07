

# Create main function that passes payroll function into variable and prints result.
def main():
    wage = payroll()
    print(wage)

# Create a payroll function that takes user input for hours and returns total pay to user.

def payroll():
# Take user input for hours and rate
    hrs = input("Enter Hours:")
    rte = input("Enter Rate:")
# Convert user input to float
    hours = float(hrs)
    rate = float(rte)


# Create Boolean expression to calculate total pay and return overtime and regulary pay to user.
    if hours > 40:
        regular_pay = 40 * rate 
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
        return total_pay
    else:
        return hours * rate

# Call main function

main()
