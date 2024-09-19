		
phonebook()
		

def nokia():
	menu = '''

	Welcome to Nokia 3310 !

	please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		1 >>> Phone Book
		2 >>> Message
		3 >>> Chat
		4 >>> Call Register
		5 >>> Tones
		6 >>> Settings
		7 >>> Call Divert
		8 >>> Games
		9 >>> Calculator 
		10 >>> Remainder
		11 >>> Clock
		12 >>> Profiles
		13 >>> SIM Services
:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
print(menu)

phone_book = int(input("Enter from 1 to 13:"))

match phone_book: 
	case 1: 
		phone_book_menu = '''
	

	Welcome to the Phone Book Menu !
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Search
	2 >>> Service Nos
	3 >>> Add Name
	4 >>> Erase
	5 >>> Edit
	6 >>> Assign Tone
	7 >>> Send b'card
	8 >>> Options
	9 >>> Speed Dials
	10 >>> Voice Tags
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
	print(phone_book_menu)
		phone_book_choice = int(input("Enter from 1 to 10:"))

		match phone_book_choice:
			case 1: print("Search") 			
			case 2: print("Service Nos") 							
			case 3: print("Add Names") 				
			case 4: print("Erase")
			case 5: print(Edit+"")
			case 6: print("Assign Tone")
			case 7: print("Send b'card")
			case 8:
				String option_drop_down = '''
				Please select the menus below to continue:
											                      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	
				1 >>> Type Of Views
				2 >>> Memory Status
												              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

				'''

			print(option_drop_down)		

			int choice = int(input("Enter from 1 to 13:")) 

				switch choice:
					case 1: 
						print("Type Of View") 
							
					case 2: 
						print("Memory Status") 
					
					default: 
						print("You have entered an invalid number! start again!!") 
					
			case 9: 
				print("Speed Dials")

			case 10: 
				print("Voice Tags") 
	
			default: 
				print("You have entered an invalid number! start again!!")








	
	"""case 2: 
		message = '''Welcome to Messages

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Write Messages
	2 >>> Inboxq
	3 >>> Outbox
	4 >>> Picture Messages
	5 >>> Templates
	6 >>> Smileys
	7 >>> Message Settings
	8 >>> Info Service
	9 >>> Voice Mailbox Number
	10 >>> Service Command Editor
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''

		print(message)
	case 3: 
		chat = '''Welcome to chat

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Chat
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(chat)
	case 4: 
		call_register = '''Welcome to Call Register

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Missed Calls
	2 >>> Recieved Calls
	3 >>> Dialled Numbers
	4 >>> Erase Recent Call Lists
	5 >>> Show Call Duration
	6 >>> Show Call Cost
	7 >>> Call Cost Settings
	8 >>> Prepaid Credit
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(call_register)

	
	case 5: 
		tones = '''
	Welcome to Tones

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Ringing Tone
	2 >>> Ringing Volume
	3 >>> Incoming Call Alert
	4 >>> Composer
	5 >>> Message Alert Tone
	6 >>> Keypad Tones
	7 >>> Warning And Game Tones
	8 >>> Vibrating Alert
	8 >>> Screen Saver
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	''' 
		print(tones)

	
	case 6: 
		settings =  '''Welcome to Settings

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Call Settings
	2 >>> Phone Settings
	3 >>> Security Settings
	4 >>> Restore Factory Settings
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	''' 
		print(settings)


	
	case 7: 
		call_divert = '''Welcome to Call Divert

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Call Divert
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''

		print(call_divert)

	
	case 8: 
		games = '''
	Welcome to Games

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Games
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(games)


	
	case 9: 
		calculator = '''
	Welcome to Calculator

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Calculator
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(calculator)

	
	case 10: 
		remainder = '''
	Welcome to Remainders

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Remainders
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(ramainder)

	
	case 11: 
		clock = '''Welcome to Clock

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Clock
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	''' 
		print(clock)

	
	case 12: 
		profiles = '''Welcome to Profiles

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> Profiles
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''
		print(profiles)

	
	case 13: 
		sim_service = '''Welcome to SIM Service

	Please select the menus below to continue:
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	1 >>> SIM Service
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	'''

		print(sim_service)"""

'''