import base64

class Encript:

		# Encode string
	@staticmethod
	def encode(value):
		return base64.b64encode((value.encode('utf-8')))
	
		# Decode String
	@staticmethod
	def decode(value):
		return base64.b64decode((value.encode('utf-8'))).decode("UTF-8")
