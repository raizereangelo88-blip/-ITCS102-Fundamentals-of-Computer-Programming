#Ask user to input ten 10 numbers - checked
#after that summation of all ten 10 numbers
sum = 0
for x in range(1,20,1):
    print (x)
    number = eval(input("Enter number --> "))
    sum += number

print ("The sum of all numbers is", sum)