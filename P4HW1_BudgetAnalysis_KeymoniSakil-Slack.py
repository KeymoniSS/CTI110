# This program keeps the running total that a user has budgeted in a month and output the amount that they are either under or over budget.
# September 24, 2018
# CTI-110 P4HW1 - Budget Analysis
# Keymoni Sakil-Slack
#

budget = float(input('Enter your budget for the month: $'))

# Create a variable to control the loop
keep_going = 'y'
total = 0

# Calculate the expense
while keep_going == 'y':
    expense = float(input('Enter your expense(s) for the month: $'))
    keep_going = input('Do you want to calculate another ' + \
                   'expense (Enter y for yes/n for no): ')
    
#Add expenses onto each other
    total = total + expense

print('You spent $', \
      format(total, ',.2f'), sep='')

#Calculate to determine if under or over budget
over_budget = budget + total
under_budget = budget - total

#Create if functions
if budget > total:
    print('You are under budget by $',under_budget)
          
elif budget < total:
    print('You are over budget by $',over_budget)

else:
    print('You are neither under or over budget')
          
# Pseudocode:
# Set total = 0
# Prompt the user for the budget for the month
# Prompt the user for the expenses for the month
# Add expenses to total
# Display total and determine if user is under or over budget

