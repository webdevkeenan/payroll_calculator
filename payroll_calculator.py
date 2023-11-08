# Create main function to ask user for input and return value.
def main():
    wages = payroll()
    print(f"Total Pay:$ {wages:.2f}")

# Create payroll function. Get user input. 
def payroll():
    hrs = input("Enter Hours Worked:")
    rte = input("Enter Rate of Pay:")
# Convert user input to float.
    hours = float(hrs)
    rate = float(rte)

# Use boolean statement to return overtime pay and regular pay to user.
    if hours > 40:
        regular_pay = 40 * rate
        overtime = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime
    else:
        total_pay = hours * rate

# return total pay.
    return total_pay


# call main function.

main()
