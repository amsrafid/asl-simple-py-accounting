import datetime
from controller.account import Account
from model.Deposite import Deposite as Deposites

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

			accountAll = Account().all()
			accountAll[acc]['balance'] = str(int(accountAll[acc]['balance']) + int(amount))
			
			Account().setData(accountAll)

			print("Deposite is created successfully.\n")
		
		else:
			print("Account is not valid.")
