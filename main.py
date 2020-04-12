class User:
	def __init__(self, number = '', name = '', age = '', phone = '', balance = ''):
		self.number = number
		self.name = name
		self.age = age
		self.phone = phone
		self.balance = balance

	def create(self):
		if( (self.number) in account.keys()):
			return False
		else:
			account[self.number] = {
				'number' : self.number,
				'name' : self.name,
				'age' : self.age,
				'phone' : self.phone,
				'balance' : self.balance
			}
			return True

	def edit(self):
		pass

	def show(self, accNumber):
		if(accNumber in account.keys()):
			return account[accNumber]
		else:
			return "\nAccount is not found\n"

accountFields = ['number', 'name', 'age', 'phone', 'balance']
accountdata = {}
account = {}

while(1):
	print('Press,\n1 - to show user\n2 - to create user\n3 - to edit user\n0 to exit')
	action = input("Action number is: ")

		# Create new Account
	if(action == '1'):
		user = User()
		print(user.show(input("Enter user account number: ")))

	elif(action == '2'):
		for n in range(len(accountFields)):
			accountdata[accountFields[n]] = input("Account " + accountFields[n] + ": ")
			
		user = User(accountdata['number'], accountdata['name'], accountdata['age'], accountdata['phone'], accountdata['balance'])
		
		if(user.create() == True):
			print("\nNew User created.\n")
		else:
			print("\nUser is already exists\n")

		# Exit
	else:
		break

print("Thanks.")