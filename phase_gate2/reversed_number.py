def reverse(number):
  number_reversed = 0
  number = int(input("Enter the number to be reversed: "))

  while number != 0:
    digit = number % 10
    number_reversed = number_reversed * 10 + digit
    number //= 10

  return number_reversed


reverse(456)
print(f"{reverse}")