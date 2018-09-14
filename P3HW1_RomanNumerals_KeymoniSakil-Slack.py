# This program will display the Roman Numerals for the integers 1 through 10
# CTI-110 
# P3HW1 - Roman Numerals 
# Keymoni Sakil-Slack 
# September 14, 2018
#

#Ask for a number 1 through 10.
integer = int(input('Enter a number within a range of 1 through 10: '))

#Set conditions.
if 0 < integer < 11:
    print('Calculating...')
    
#If values meet conditions.
if integer == 1:
    print('The Roman Numeral for this number is: I')
elif integer == 2:
    print('The Roman Numeral for this number is: II')
elif integer == 3:
    print('The Roman Numeral for this number is: III')
elif integer == 4:
    print('The Roman Numeral for this number is: IV')
elif integer == 5:
    print('The Roman Numeral for this number is: V')
elif integer == 6:
    print('The Roman Numeral for this number is: VI')
elif integer == 7:
    print('The Roman Numeral for this number is: VII')
elif integer == 8:
    print('The Roman Numeral for this number is: VIII')
elif integer == 9:
    print('The Roman Numeral for this number is: IX')
elif integer == 10:
    print('The Roman Numeral for this number is: X')
#If values doesn't meet conditions; display error message.
else:
    print('Error: Number must be within the range of 1 through 10')

# Pseudocode:
# Prompt user to enter an interger for the numbers 1 through 11
# integer = input "Enter a number within a range of 1 through 10:"
# If the integer is greater than 0 and less than 11
#   Print "Calculating..."
# elif 1 is pressed Print "The Roman Numeral for this number is: I"
# elif 2 is pressed Print "The Roman Numeral for this number is: II"
# elif 3 is pressed Print "The Roman Numeral for this number is: III"
# elif 4 is pressed Print "The Roman Numeral for this number is: IV"
# elif 5 is pressed Print "The Roman Numeral for this number is: V"
# elif 6 is pressed Print "The Roman Numeral for this number is: VI"
# elif 7 is pressed Print "The Roman Numeral for this number is: VII"
# elif 8 is pressed Print "The Roman Numeral for this number is: VIII"
# elif 9 is pressed Print "The Roman Numeral for this number is: IX"
# elif 10 is pressed Print "The Roman Numeral for this number is: X"
# Else
#   Print "Error: Number must be within the range of 1 through 10"

