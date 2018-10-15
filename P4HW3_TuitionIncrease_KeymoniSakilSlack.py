# This codes displays the projected semester tuition amount for the next 5 years.
# September 26, 2018
# CTI-110 P4HW3 - Tuition Increase
# Keymoni Sakil-Slack
#

print('These are the projected semester tuition amount for the next 5 years')
for year in range (1, 6):
    rate = .03
    tuition= 8000
    total =((tuition * rate)*year) + tuition
    print('The projected semester tuition for year', year, 'is $', total )

# Pseudocode:
# Create a range for 1 through 5.
# Calculate the total for the tuititon plus 3% of the tuition, per year.
# Display the output.
