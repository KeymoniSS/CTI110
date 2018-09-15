# This program will display the shipping charges depending on a given weight in pounds
# CTI-110 
# P3HW2 - Shipping Charges 
# Keymoni Sakil-Slack 
# September 14, 2018
#

print('\nWelcome to Fast Freight Shipping Company')
print('--------------------------------------------------------------------------------')

#Prompt user for weight of a package.
weight = float(input('To find the shipping cost of a package please enter the weight of the package in pounds: '))

#Calculate the rate per pound for each condition and set variables for each condition
shipping_charge1 = 1.50 * weight
shipping_charge2 = 3.00 * weight
shipping_charge3 = 4.00 * weight
shipping_charge4 = 4.75 * weight


print('\nCalculating...')
#Set Conditions for ifs, elifs, and else:

#If weight = 0 display error
if weight ==0:
    print('Error: In order for shipping charges to apply, the package must weighs over 0 pounds/lb.')
#2 pounds or less
elif 0 < weight < 3:
    print('The cost of shipping for this package is: $', format(shipping_charge1, ',.2f'))
#Over 2 pounds but not more than 6 pounds
elif 2 < weight < 7:
    print('The cost of shipping for this package is: $', format(shipping_charge2, ',.2f'))
#Over 6 pounds but not more than 10 pounds
elif 6 < weight < 11:
    print('The cost of shipping for this package is: $', format(shipping_charge3, ',.2f'))
#Over 10 pounds
else:
    print('The cost of shipping for this package is: $', format(shipping_charge4, ',.2f'))
    
#Present error message if package is less than 0 as well
if weight < 0:
    print('Error: In order for shipping charges to apply, the package must weighs over 0 pounds/lb.')

print('\nThank you have a nice day!')




# Pseudocode:
# Print "Welcome to Fast Freight Shipping Company" and add line break
# Prompt user to enter a weight of a package in pounds
# Get the weight
# Save input
# Calculate the rate per pound for each condition and set variables for each condition
# Get the rate per pound for shipping_charge1
# Get the rate per pound for shipping_charge2
# Get the rate per pound for shipping_charge3
# Get the rate per pound for shipping_charge4
# Save values
# Set Conditions for ifs, elifs, and else:
# If the input weight = 0 display error
#
# Else-if (elif) the input weight is 2 pounds or less:
#                Print "The cost of shipping for this package is: $" + Display the result for shipping_charge1
#
# Else-if (elif) the input weight is over 2 pounds but not more than 6 pounds:
#                Print "The cost of shipping for this package is: $" + Display the result for shipping_charge2
#
# Else-if (elif) the input weight is over 6 pounds but not more than 10 pounds:
#                Print "The cost of shipping for this package is: $" + Display the result for shipping_charge3
#
# Else if the input weight is over 10 pounds:
#                Print "The cost of shipping for this package is: $" + Display the result for shipping_charge4
#
# Present error message if package is less than 0 as well
#
# Print "Thank you have a nice day!"



