# This program takes an integer inputted by the user and returns true if the argument is a prime number or false if it is not.
# October 1, 2018
# CTI-110 P5HW1 - Prime Numbers
# Keymoni Sakil-Slack
#

# main function
def main():
    # Get a number from the user
    number = int(input('Enter a number: '))
    if is_prime(number):
        print('The number is prime.')
    else:
        print('The number is not prime.')

    
def is_prime(number):
    # Determine whether number is prime. If it is,
    # set status to false. Otherwise, set status
    # to true.
    if (number % 2) == 0:
        status = False
    else:
        status = True
    # return the value of the status variable.
    return status

main()

# Pseudocode:
# Input number
# Set condition and status
# Return status
# Outputs either true or false argument
