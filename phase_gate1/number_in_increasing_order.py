integer_one = int(input("Enter the first digit number: "))
integer_two = int(input("Enter the second digit number: "))
integer_three = int(input("Enter the third digit number: "))


if integer_one > integer_two:
    integer_one, integer_two = integer_two, integer_one
if integer_one  > integer_three:
    integer_one, integer_three = integer_three, integer_one
if integer_two > integer_three:
    integer_two, integer_three = integer_three, integer_two

print(f"{"The increasing order of three integers are: "}{integer_one} {integer_two}{integer_three}")