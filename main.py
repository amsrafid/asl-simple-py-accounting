class User:
	def __init__(self, number, name, age, phone, balance):
		self.number = number
		self.name = name
		self.age = age
		self.phone = phone
		self.balance = balance

	def create(self):
		if( self.number in account.keys()):
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

accountFields = ['number', 'name', 'age', 'phone', 'balance']
accountdata = {}
account = {}

while(1):
	print('Press,\n1 to create user\n2 to edit user\n0 to exit')
	action = int(input("Action number is: "))

		# Create new Account
	if(action == 1):
		for n in range(len(accountFields)):
			accountdata[accountFields[n]] = input("Account " + accountFields[n] + ": ")
			
		user = User(accountdata['number'], accountdata['name'], accountdata['age'], accountdata['phone'], accountdata['balance'])
		
		if(user.create() == True):
			print("New User created.")
		else:
			print("User is already exists")

		# Exit
	else:
		break

print("Thanks.")