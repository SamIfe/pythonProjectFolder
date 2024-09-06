score = int(input("Enter score: "))

result = ""
if score >= 40:
	result = "passed"
	print("Really", result)

if score < 40:
	result = "failed"
	print("really", result)