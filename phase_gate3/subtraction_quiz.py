import random
welcome = """
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	WELCOME TO THE SUBSTRACTION QUIZ!


	>>. Ensure that you attempt all questions

	>>. You will be given 10 random subtraction problems.

	>>. You can attempt each problem up to 10 times.

			Goodluck!!
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
print (welcome)
total_score = 0
total_question = 10

for exam in range(total_question):
  first_rand_number = random.randint (1, 100)
  second_rand_number = random.randint (1, first_rand_number)

  correct_answer = first_rand_number - second_rand_number
  attempt_question = 0 
  correct_attempt = False

  print(f" Question {exam + 1}: What is {first_rand_number} - {second_rand_number}? ")

  while attempt_question < 10 and not correct_attempt:
    candidate_answer = int(input(f"Attempt question {attempt_question + 1}: your answer: "))

    try:
      if candidate_answer == correct_answer:
        print("Correct\n")
        total_score += 1
        correct_attempt = True
      else:
        print("Incorrect. Try again.")
    except ValueError:
      print("Please enter a valid integer.")
        
    attempt_question += 1
  if not correct_attempt:
    print(f"The correct answer was {correct_answer}.\n")
print(f"This is the end of the quiz!! Your score id {total_score} out of {total_question}.")


    


  
  