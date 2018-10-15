# This progam accepts a number of feet as an argument and returns the number of inches in that many feet.
# October 1, 2018
# CTI-110 P5T2_FeetToInches 
# Keymoni Sakil-Slack
#

# Create constant for the number of inches per foot
INCHES_PER_FOOT = 12

# main function
def main ():
    # Get a number of feet from the user
    feet = int(input('Enter a number of feet: '))

    #Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches funcion converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()

# Pseudocode:
# Input feet
# Convert feet to inches
# Display inches

