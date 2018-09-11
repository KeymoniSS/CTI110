# This program should display the percentage of males and females in a class
# September 10, 2018
# CTI-110 P2HW2 - Male Female Percentage
# Keymoni Sakil-Slack
#

#Input number of males and females
number_of_males = float(input('Enter the total number of males: '))
number_of_females = float(input('Enter the total number of females: '))

#Calculate the sum of the two inputs
sum = number_of_males + number_of_females

#Calculate the percentages of inputs
percentage_of_males = (number_of_males / sum)
percentage_of_females = (number_of_females / sum)

#line-break
print ('\n')

#Display output
print('The percentage of males:', format(percentage_of_males, '.0%'))
print('The percentage of females:', format(percentage_of_females, '.0%'))


# Prompt for the total number of males
# Save value
# Prompt for the total number of females
# Save value
# Calculate the sum of the two inputs
# Calculate the percentages of males as the number of males divided by the sum
# Calculate the percentages of females as the number of females divided by the sum
# Save values
# Display the percentage of males
# Display the percentage of females
