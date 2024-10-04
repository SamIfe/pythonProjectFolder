import math
def divide_or_square(number):
  number = float(input("Enter number to be squared: "))
  
  if number < 0:
    return "input must be positive and not a negative value;/                      please enter a positive value: "
  if number % 5 == 0:
    result = math.sqrt(number)
    return result
  else:
    return number % 5
print(divide_or_square(10))