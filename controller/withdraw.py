import datetime
from controller.account import Account
from model.Withdraw import Withdraw as Withdraws
from model.Statement import Statement as Statements

class Withdraw:

	@staticmethod
	def create():
		acc = input("\nEnter Account Number: ")
		account = Account().find(acc)

		if(account):
			amount = input("Enter amount: ")
			
			withdraw = Withdraws()
			withdraw.create({
				'account' : acc,
				'amount' : amount,
				'date' : str(datetime.date.today())
			})

			Statements().create({
				'account' : acc,
				'amount' : amount,
				'status' : 'debit',
				'date' : str(datetime.date.today())
			})

			accountAll = Account().all()
			accountAll[acc]['balance'] = str(int(accountAll[acc]['balance']) - int(amount))
			
			Account().setData(accountAll)

			print("Withdraw is created successfully.\n")
		
		else:
			print("Account is not valid.")

	@staticmethod
	def show(acc):
		account = Account().find(acc)
		print("\nWithdraw of " + account['name'])

		withdraw = Withdraws().all()
		done = True
		
		depKey = list(withdraw.keys())

		num = 1
		for i in range(len(depKey)):
			if(str(withdraw[depKey[i]]['account']) == str(acc)):
				done = False
				print(str(num) + ": " + str(withdraw[depKey[i]]['date']) + " BDT-" + str(withdraw[depKey[i]]['amount']))
				num += 1

		if(done):
			print("\nNo withdraw is found.")

		print("\n")
