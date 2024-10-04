def summation_of_string_value(number1, number2)-> str:
 try:
  number1 = int(number1)
  number2 = int(number2)
  summation = number1 + number2
  return str(summation)
 except ValueError:
  return "Invalid submission, please imput the value as string: "

print(summation_of_string_value("4", "8"))