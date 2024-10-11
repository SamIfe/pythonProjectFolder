#number = int(input("Enter parttern range: "))

for parttern in range (5):
    print(" ")
    for number1 in range(1, parttern + 2):
        if number1 % 2 == 0:
            print("*", end = " ")
        else:
            print (number1, end = " ")


for parttern2 in range (5, 0, -1):
    print(" ")
    for number2 in range(1, parttern2 + 1):
        if number2 % 2 == 0:
            print("*", end = " ")
        else:
            print (number2, end = " ")