number = int(input("Enter parttern range: "))
for parttern in range (number):
  for number in range(parttern + 1):
    if number % 2 == 0:
      print(number + 1, end = " ")
    else:
      print ("*", end = " ")
  print()