
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

# Multiply hours and rate to calculate regular pay.
    regular_pay = hours * rate

# Create Boolean expression to calculate and return total pay to user. 
    if hours > 40:
        overtime = (regular_pay - 40) * (rate * 1.5)
        overtime_pay = overtime + regular_pay
        total_pay = overtime_pay * regular_pay
    else:
        total_pay = regular_pay
    

    return total_pay
