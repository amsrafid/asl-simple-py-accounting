from model.Models import Models

class Withdraw(Models):
	
	table = 'table/withdrawTable'

	def __init__(self):
		super().__init__(self.table, 'withdraw')
