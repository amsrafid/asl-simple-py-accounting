import subprocess as sp

from controller.auth import Authentication
from controller.operation import Operation

def main():
	
	auth = False

	while(1):
		if(auth):
			op = Operation.operate()
			if op == 'operate':
				continue
			elif op == 'logout':
				auth = False
				continue
			elif op == 'clear':
				sp.call('cls', shell = True)
				continue
			else:
				break
		else:
			auth = Authentication.check()

	print("Thanks.")

if(__name__ == '__main__'):
	main()
