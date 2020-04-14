class User:
	
	accountFields = ['number', 'name', 'age', 'phone', 'balance']
	userData = {}

	def get(self):
		for acc in range(len(self.accountFields)):
			self.userData[self.accountFields[acc]] = input("Enter " + self.accountFields[acc] + ": ")
		
	def getNumber(self):
		return self.userData['number']
		
	def getName(self):
		return self.userData['name']
		
	def getAge(self):
		return self.userData['age']
		
	def getPhone(self):
		return self.userData['phone']
		
	def getBalance(self):
		return self.userData['balance']
