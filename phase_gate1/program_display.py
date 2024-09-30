# Write a program that displays the following table


#first_input = int(input("Enter the first input: "))

print(f"{"a":<10} {"b":<12} {"a**b"}")
for number in range (1, 6):
	result1 = number
	result2 = result1 + 1
	result3 = result1 ** (result1 + 1)
	print(f"{result1:<11}{result2:<15}{result3}")
	