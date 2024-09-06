language =input("Enter preferred language: ")

match language:
	case "java":
		print("You can't break united folks")

	case "python":
		print("If it's working well, don't touch it")

	case "javascript":
		print("Do not spread the story that will break the nation!")

	case _:
		print("it executes this when there's no valid case")
