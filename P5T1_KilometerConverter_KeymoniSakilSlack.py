# This program asks for the user to input a distance in kilometers, converts that distance to miles, and outputs it.
# October 1, 2018
# CTI-110 P5T1_KilometerConverter 
# Keymoni Sakil-Slack

# Make constant
CONVERSION_FACTOR = 0.6214

# Ask for user input
def main ():
    #Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))
    
    # Display the distance converted to miles
    show_miles(kilometers)

def show_miles (km):
    #Calculate miles
    # Formula is miles = kilometers X 0.6214
    miles = km * CONVERSION_FACTOR

    #Display the miles
    print(km, 'kilometers equals', miles , 'miles.')
    
# Call the main function
main()

# Pseudocode:
# Input kilometers
# Convert kilometers to miles
# Display miles
