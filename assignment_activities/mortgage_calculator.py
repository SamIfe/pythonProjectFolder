'''
Prompt user to enter principal amount
Store the variable as principal_amount

Prompt user to enter interest rate
Store the variable as interest_rate

Prompt the user to enter loan duration
Store the variable as loan_duration

Calculate monthly_rate equals interest_rate divide by 100 divided by 12
Calculate duration_of_loan equals loan_duration multiply by 12

Variable power_rate1 equals 1 plus month_rate
Variable power_rate2 equals power_rate1 raise to power duration_of_loan
Variable monthly_payment_value equals pincipal_amount multiply by monthly_rate multiply by power_rate2 divided by power_rate2 minus 1

Display the result '''



import math

principal_amount = int(input("Enter the principal amount: "))

interest_rate = int(input("Enter the interest rate: "))

loan_duration = int(input("Enter loan duration: "))

monthly_rate = (interest_rate / 100) /12

duration_of_loan = loan_duration * 12

power_rate1 = 1+ monthly_rate

power_rate2 = math.pow(power_rate1, duration_of_loan)

monthly_payment_value = (principal_amount * monthly_rate * power_rate2) / (power_rate2 - 1)

print ("Your Monthly Payment is: $",(round(monthly_payment_value, 2)))