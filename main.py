from model.user import User
from controller.account import Account
from library.file import File
from library.action import Action

def main():
	while(1):
		
		action = Action().get()

			# Show Single User
		if(action == '1'):
			Account.show()
			
			# Create new User
		elif(action == '2'):
			user = User()
			user.get()							# input user data
			Account.create(user) 		# Create a new account

			# Edit User
		elif(action == '3'):
			user = User()
			user.get()							# input user data
			Account.edit(user) 		# Create a new account

			# Delete Account
		elif(action =='4'):
			Account.delete(input('Enter Account Number: '))

			# Show All user
		elif(action == '5'):
			print(Account.all())

			# Exit
		else:
			break

	print("Thanks.")


if(__name__ == '__main__'):
	main()
