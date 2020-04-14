from library.file import File
from model.user import User

""" 
	Account Management
 """
class Account:

	""" 
		Create new Account
	 """
	@staticmethod
	def create(user):
		account = File.read('table/accountTable')

		if( (user.getNumber()) in account.keys()):
			print("\nUser is already exists\n")
			return False
		else:
			account[user.getNumber()] = {
				'number' : user.getNumber(),
				'name' : user.getName(),
				'age' : user.getAge(),
				'phone' : user.getPhone(),
				'balance' : user.getBalance()
			}

			File.write('table/accountTable', account)

			print("\nNew Account has been created successfully.\n")
			return True

	""" 
		Edit existing account
	 """
	def edit(self):
		pass

	""" 
		Show a single Account
	 """
	@staticmethod
	def show():
		accNumber = input("Enter account Number: ")
		account = File.read('table/accountTable')

		if(accNumber in account.keys()):
			print("\n")
			Account.viewSingle(account[accNumber])
		else:
			print("\nAccount is not found\n")

	""" 
		Delete an existing account
	 """
	def delete(self):
		pass

	""" 
		View Single account details
	 """
	@staticmethod
	def viewSingle(acc):
		user = User()
		for fields in range(len(user.accountFields)):
			print("Account " + user.accountFields[fields] + ": " + acc[user.accountFields[fields]])
		
		print("\n")
