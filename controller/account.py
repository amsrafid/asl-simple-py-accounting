from library.file import File
from model.user import User

""" 
	Account Management
 """
class Account:

	@staticmethod
	def all():
		return File.read('table/accountTable')

	""" 
		Create new Account
	 """
	@staticmethod
	def create(user):
		account = File.read('table/accountTable')

		if( (user.getNumber()) in account):
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

	
		# Edit existing account
	
	@staticmethod
	def edit(user):
		account = File.read('table/accountTable')

		if( user.getNumber() in account):
			if(user.getName()):
				account[user.getNumber()]['name'] = user.getName()
			if(user.getAge()):
				account[user.getNumber()]['age'] = user.getAge()
			if(user.getPhone()):
				account[user.getNumber()]['phone'] = user.getPhone()
			if(user.getBalance()):
				account[user.getNumber()]['balance'] = user.getBalance()

			File.write('table/accountTable', account)

			print("\nAccount has been updated successfully.\n")
			return True
		else:
			print("\nAccount is not exists.\n")
			return False

	
		# Show a single Account
	
	@staticmethod
	def show():
		accNumber = input("Enter account Number: ")
		account = File.read('table/accountTable')

		if(accNumber in account):
			print("\n")
			Account.viewSingle(account[accNumber])
		else:
			print("\nAccount is not found\n")

	""" 
		Delete an existing account
	 """
	@staticmethod
	def delete(number):
		account = File.read('table/accountTable')
	
		if(number in account):
			del account[number]
			File.write('table/accountTable', account)
			print('Account number ' + number + " is deleted successfully.")
			return True

		else:
			print("Account number is not registred.")
			return False

		# View Single account details
	
	@staticmethod
	def viewSingle(acc):
		user = User()
		for fields in range(len(user.accountFields)):
			print("Account " + user.accountFields[fields] + ": " + acc[user.accountFields[fields]])
		
		print("\n")
