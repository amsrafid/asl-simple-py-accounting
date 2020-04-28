from model.Models import Models

class Statement(Models):
	
	table = 'table/statementTable'

	def __init__(self):
		super().__init__(self.table, 'statement')
