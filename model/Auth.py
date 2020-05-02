from model.Models import Models

class Auth(Models):
	
	table = 'table/authTable'

	def __init__(self):
		super().__init__(self.table, 'auth')
