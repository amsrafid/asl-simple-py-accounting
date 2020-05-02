class Action:

	action = {
		'1' : 'to show account',
		'2' : 'to create account',
		'3' : 'to edit account',
		'4' : 'to delete account',
		'5' : 'to show all account',

		'6'	:	'to deposite',
		'7'	:	'to show deposits',

		'8'	:	'to withdraw',
		'9'	:	'to show withdraws',

		'10'	:	'to register',
		'11'	:	'to show authenticated user',

		'20' : 'to logout',
		'21' : 'to clear screen',
		'0' : 'to exit'
	}

	def __init__(self):
		
		key = list(self.action.keys())
		actionSetStr = ""
		
		for ac in range(len(key)):
			actionSetStr += "\n" + str(key[ac]) + " - " + self.action[key[ac]]
			
		print('Press,' + actionSetStr)

	def get(self):
		return input("Action number is: ")
