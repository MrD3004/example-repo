import math

print("Choose a calculation:")
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")   #The program starts by displaying options for the user to choose investment or bond.
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

if choice == "investment":
    # Investment calculation
    principal = float(input("Enter the amount you are investing: "))
    rate = float(input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan to invest: "))
    
    interest_type = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").strip().lower() #The user's input is converted to lowercase using .strip().lower() so variations like INVESTMENT, Investment, or investment are accepted.
    if interest_type == "simple":
        total = principal * (1 + (rate / 100) * years)   #If the user selects investment:
                                                         #They choose between simple or compound interest, and the program calculates and outputs the total amount 
                                                         # based on the respective formula.
                                                         #The user inputs the deposit amount, interest rate, and number of years.


    elif interest_type == "compound":
        total = principal * (1 + rate / 100) ** years
    else:
        total = None
        print("Invalid interest type selected!")
    
    if total:
        print(f"Total amount after {years} years: {total:.2f}")

elif choice == "bond":
    # Bond calculation If the user selects bond: 
    # The user provides the house value, annual interest rate, and repayment period in months.
    # The program calculates the monthly repayment using the specified formula.
    house_value = float(input("Enter the value of the house: "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
    months = int(input("Enter the number of months you plan to repay the loan: "))
    
    monthly_rate = annual_rate / 12 / 100
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months))
    print(f"Your monthly repayment is: {repayment:.2f}")
    
else:
# If the user enters invalid options (e.g., invalid choice or interest type), the program displays an error message.
    print( "Invalid choice. Please restart the program and choose either investment or bond")

