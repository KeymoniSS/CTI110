# This code displays a table of the celsius temperatures 0 through 20 and their fahrenheit equivalents. 
# September 26, 2018
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Keymoni Sakil-Slack
#

# Print the heading for the table
print()
print('Celsius\tFahrenheit')
print('-------------------')

# Convert celsius to fahrenheit
for celsius in range(0, 21):
    fahrenheit = (9/5)*celsius + 32
    print(celsius, '\t', fahrenheit)
    
# Pseudocode:
# Print the heading for the table
# Print numbers 0 through 20
# Plug these numbers into the celsius to fahrenheit formula
# Print the table
