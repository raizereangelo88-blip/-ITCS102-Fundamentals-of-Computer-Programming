from getpass import getpass

username = 'rai'
password = 'ewankohindikoalam'

u = input("username  --> ")
p = getpass("password --> ")

if  (u == username) and (p == password):
 			print("Access Granted")
else: 
			print("Access Denied")

