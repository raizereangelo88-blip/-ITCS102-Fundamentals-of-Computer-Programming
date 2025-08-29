name = input("Please input your name --> ")
fare = eval(input("How much is your fare fee? --> ") )
isStudent = input("Are you a currently a student (yes / no ) ")

if isStudent.lower() == "yes":
	discount = fare * 0.2 
	new_fare = fare - discount
	print("Hi",name," Your discount is ", discount,"Your new fare is ", new_fare)
else: 
	print("Hi" , name,"you're only eligible for regular price")