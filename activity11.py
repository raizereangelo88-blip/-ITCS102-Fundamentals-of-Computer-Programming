#conditional statemnts
#Ask user to input a temperature
#conditions as follow:
#Conditions as follow:
# below 0 -- freezing temperature 
# 1 - 20 -- Extremely Cold
# 21 - 30 -- Moderately Cold 
# 31 - 37 -- Lukewarm
# 38 - 45 -- Hot
# 45 - 50 -- Boiling Hot
# 51 and above -- Dangerous Temperature

temp =  eval(input("Input temperature --> ") )

if temp >= 1 or temp <= 20 :
	print ("The temperature is extremely cold")
elif temp >= 21 or temp <= 30 :
	print ("The temperature is moderately cold")
elif temp >= 31 or <= 37 : 
	print ("The temperature is Lukewarm")
elif temp >=38 or <= 45:
	print ("The temperature is Hot")
elif temp >= 45 or <= 50 :
	print ("The temperature is Boiling Hot")
elif temp >= 51 or above
	print ("The temperature is Dangerous")