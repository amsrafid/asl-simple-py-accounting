from model.user import User
from controller.account import Account
from library.file import File

def main():
	while(1):
		print('Press,\n1 - to show user\n2 - to create user\n3 - to edit user\n0 to exit')
		action = input("Action number is: ")

			# Create new Account
		if(action == '1'):
			Account.show()
			
		elif(action == '2'):
			user = User()
			user.get()							# input user data
			Account.create(user) 		# Create a new account
			
			# Exit
		else:
			break

	print("Thanks.")


if(__name__ == '__main__'):
	main()
