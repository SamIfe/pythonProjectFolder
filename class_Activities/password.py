'''
Prompt for password
Store in variable password
get the lenght of the password
Store in variable password_counts
Multiply password_counts by astericks '*'
Display password in astericks
'''


password = input("Enter your password:  ")
password_counts = len(password)
password_astericks = '*' * password_counts
print(password_astericks)

