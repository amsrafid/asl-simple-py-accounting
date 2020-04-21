class Action:

	action = {
		'1' : 'to show user',
		'2' : 'to create user',
		'3' : 'to edit user',
		'4' : 'to delete user',
		'5' : 'to show all user',

		'6'	:	'to deposite',
		'7'	:	'to show deposits',

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
