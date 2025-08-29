from getpass import getpass

username = 'Rai'
password = '5555'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")

if  (u == username) and (p == password) :
	print("Access Granted")
else:
	print("Access Denied")