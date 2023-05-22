# payProgram.py
# This program calculates weekly pay for 3 employees.
# Weekly pay is calculated by multiplying the hours worked times the pay rate


# Calculate the pay for someone from pay rate and hours worked. 
# The "name" parameter is used for the input prompt text.
def payCalc(name):
    # Get the pay rate and hours worked from user
    # (f before string is for string interpolation btw)
    payRate = input(f"Enter the pay rate for {name}> $") 
    hoursWorked = input(f"Enter the number of hours {name} worked> ")

    # Convert the input values to a floating point number to do the pay calculations
    # Then back to str because that's all we need it in. Not future proof, but it makes code more readable
    return str( float(payRate) * float(hoursWorked) )


# Print the weekly pay for Emily, Matthew, and Sarah by concatenating 
# the return value of payCalc() to the "___'s weekly pay is: " text.
print("Emily's weekly pay is: $" + payCalc("Emily"))
print() # new line
print("Matthew's weekly pay is: $" + payCalc("Matthew"))
print() # new line
print("Sarah's weekly pay is: $" + payCalc("Sarah"))







###### I think the above code is a much more elegant and scalable solution. 
###### If it has to be done closer to the way the assignment intended, here's this code:

if (False): # Just disabling this code without having annoying nested comments  
    payEmily = 0	#this variable will hold the weekly pay for Emily
    payMatthew = 0 	#this variable will hold the weekly pay for Matthew
    paySarah = 0 	#this variable will hold the weekly pay for Sarah


    ###### Emily

    #Get the pay rate and hours worked for Emily from the keyboard
    payRate = input("Enter the pay rate for Emily ")
    hoursWorked = input("Enter the number of hours Emily worked ")

    #The input function returns its values in a string format
    #Convert the input values to a floating point number to do the pay calculations
    payEmily = float(payRate) * float(hoursWorked)

    #Print the weekly pay for Emily
    print("Emily's weekly pay is: ")
    print(payEmily)

    ###### Matthew

    payRate = input("Enter the pay rate for Matthew ")
    hoursWorked = input("Enter the number of hours Matthew worked ")

    payMatthew = float(payRate) * float(hoursWorked)

    print("Matthew's weekly pay is: ")
    print(payMatthew)

    ###### Sarah

    payRate = input("Enter the pay rate for Sarah ")
    hoursWorked = input("Enter the number of hours Sarah worked ")

    paySarah = float(payRate) * float(hoursWorked)

    print("Sarah's weekly pay is: ")
    print(paySarah)