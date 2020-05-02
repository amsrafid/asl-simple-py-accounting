from library.file import File
from library.encript import Encript as en

from model.Auth import Auth

""" 
	Authentication Controller
 """
class Authentication:
	
	@staticmethod
	def register():
		name = input('\nEnter name: ')
		email = input('Enter email: ')
		address = input('Enter address: ')
		password = input('Enter password: ')

		Auth().create({
			'name' : name,
			'email' : email,
			'address' : address,
			'password' : en.encode(password)
		})
		print("\nAccount has been created successfully.\n")

	@staticmethod
	def view():
		users = Auth().all()
		keys = list(users.keys())
		count = 1

		if(len(keys) > 0):
			for i in range(len(keys)):
				print(str(count) + ". Name: " + users[keys[i]]['name'] + ". Email: " + users[keys[i]]['email'] + ". Address: " + users[keys[i]]['address'])
				count += 1
		else:
			print("No authenticated user has been registered.")

	@staticmethod
	def check():
		print("Login,")
		email = input("Enter your email address: ")
		password = input("Enter password: ")

		users = Auth().all()
		keys = list(users.keys())
		for i in range(len(keys)):
			if (email == users[keys[i]]['email']) and (str(en.encode(password)) == str(users[keys[i]]['password'])):
				return True

		print("Email and password couldn't matched.")
		return False
