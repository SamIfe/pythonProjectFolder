def summation_of_string_value(number1, number2)-> str:
   number1 = int(number1)
   number2 = int(number2)
   summation = number1 + number2
   return str(summation)

print(summation_of_string_value("4", "8"), summation_of_string_value("90", "12"), summation_of_string_value("2", "-60"))
