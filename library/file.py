import json

""" 
	File input Output
 """
class File:

	""" 
		Read a JSON file

		@param string dir FIle directory with file name

		@return dictionary
	 """
	@staticmethod
	def read(dir):
		with open('./' + dir + '.json', 'r') as file:
			return json.load(file)

	""" 
		Write a JSON Data into a Json file

		@param string 		dir 	FIle directory with file name
		@param dictinary 	data 	Dictionary data to write into dir file

		@return dictionary
	 """
	@staticmethod
	def write(dir, data):
		with open('./' + dir + '.json', 'w') as file:
			json.dump(data, file)
