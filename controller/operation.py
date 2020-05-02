from library.file import File
from library.action import Action

from model.user import User
from controller.account import Account
from controller.deposite import Deposite
from controller.withdraw import Withdraw
from controller.auth import Authentication

class Operation:

	@staticmethod
	def operate():
		action = Action().get()

			# Show Single User
		if(action == '1'):
			Account.show()
			return 'operate'
			
			# Create new User
		elif(action == '2'):
			user = User()
			user.get()							# input user data
			Account.create(user) 		# Create a new account
			return 'operate'

			# Edit User
		elif(action == '3'):
			user = User()
			user.get()							# input user data
			Account.edit(user) 			# Update account
			return 'operate'

			# Delete Account
		elif(action =='4'):
			Account.delete(input('Enter Account Number: '))
			return 'operate'

			# Show All user
		elif(action == '5'):
			print(Account.all())
			return 'operate'

			# Deposite
		elif(action == '6'):
			Deposite.create()
			return 'operate'

			# Show Deposites
		elif(action == '7'):
			Deposite.show(input('Enter Account Number: '))
			return 'operate'

			# Withdraw
		elif(action == '8'):
			Withdraw.create()
			return 'operate'

			# Show Withdraw
		elif(action == '9'):
			Withdraw.show(input('Enter Account Number: '))
			return 'operate'

			# Register Auth user
		elif(action == '10'):
			Authentication.register()
			return 'operate'

			# View Auth users
		elif(action == '11'):
			Authentication.view()
			return 'operate'

			# Logout
		elif(action == '20'):
			return 'logout'

			# Logout
		elif(action == '21'):
			return 'clear'

			# Exit
		else:
			return 'exit'
