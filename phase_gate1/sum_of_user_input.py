input_numbers = int(input("Enter number between 0 and 1000: "))
sum_of_userinput = 0


while input_numbers > 0:
    sum_of_userinput += input_numbers % 10  
    input_numbers //= 10         

print("The sum of the numbers imputed is :", sum_of_userinput)
