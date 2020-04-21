from library.file import File

class Models:
	
	actionType = ""
	tableName = ""

	def __init__(self, table, actionType):
		self.tableName = table
		self.actionType = actionType

	def all(self):
		return File.read(self.tableName)

	def create(self, dataStriped, key = ""):
		dataSet = self.all()
		key = self.primaryKey(key)

		if( key in dataSet):
			return False
		else:
			dataSet[key] = dataStriped

			self.setData(dataSet)
			return True

	def destroy(self, number):
		dataSet = self.all()
	
		if(number in dataSet):
			del dataSet[number]

			self.setData(dataSet)
			return True

		return False
		
		# Find a single Data

	def find(self, number):
		dataSet = self.all()

		if(number in dataSet):
			return dataSet[number]
		
		return False

		# Auto generate Primary Key
		
	def primaryKey(self, val = ""):
		if(val == ""):
			if(self.all() == {}):
				return '1'

			allData = list((self.all()).keys())
			key = allData[-1]
			return str(int(key) + 1)
		
		return val

		# Update Data

	def update(self):
		pass

		# Save data to table

	def setData(self, data):
		File.write(self.tableName, data)
