import datetime
from controller.account import Account
from model.Deposite import Deposite as Deposites
from model.Statement import Statement as Statements

class Deposite:

	@staticmethod
	def create():
		acc = input("\nEnter Account Number: ")
		account = Account().find(acc)

		if(account):
			amount = input("Enter amount: ")
			
			deposite = Deposites()
			deposite.create({
				'account' : acc,
				'amount' : amount,
				'date' : str(datetime.date.today())
			})

			Statements().create({
				'account' : acc,
				'amount' : amount,
				'status' : 'credit',
				'date' : str(datetime.date.today())
			})

			accountAll = Account().all()
			accountAll[acc]['balance'] = str(int(accountAll[acc]['balance']) + int(amount))
			
			Account().setData(accountAll)

			print("Deposite is created successfully.\n")
		
		else:
			print("Account is not valid.")

	@staticmethod
	def show(acc):
		account = Account().find(acc)
		print("\nDeposits of " + account['name'])

		deposite = Deposites().all()
		done = True
		
		depKey = list(deposite.keys())

		num = 1
		for i in range(len(depKey)):
			if(str(deposite[depKey[i]]['account']) == str(acc)):
				done = False
				print(str(num) + ": " + str(deposite[depKey[i]]['date']) + " BDT-" + str(deposite[depKey[i]]['amount']))
				num += 1

		if(done):
			print("\nNo deposite is found.")

		print("\n")