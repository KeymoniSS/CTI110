# This program keeps a running total of the number of bugs collected during seven days.
# September 24, 2018
# CTI-110 P4T2 - Bug Collector
# Keymoni Sakil-Slack
#

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day
for day in range(1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)

    #Input the number of bugs.
    bugs = int(input())

    #Add bugs to total
    total += bugs

#Display the total bugs.
print('You collected a total of', total, 'bugs.')    


# Pseudocode: 
# Set total = 0
# for each of 7 days:
#       Input bugs collected for aday
#       Add bugs collected to total
# Display total
