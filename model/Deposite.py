from model.Models import Models

class Deposite(Models):
	
	table = 'table/depositeTable'

	def __init__(self):
		super().__init__(self.table, 'deposite')
