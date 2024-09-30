import random

number_one = random.randint(0, 99)
number_two = random.randint(0, 99)

print(f"What is the expected sum of  {number_one} and {number_two}?: ")

user_response = int(input("Enter your answer: "))
	
correct_response = number_one + number_two
correct_answer = (user_response == 	correct_response)

print("Your answer is:", correct_answer)
