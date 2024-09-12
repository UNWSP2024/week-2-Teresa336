#Programmer: Teresa Fischer
#Date: 9/12/2024
#Title: Program #2: Average Age

def average_age():
    # Get User Input
    age_1 = int(input('Enter age of friend 1:'))
    age_2 = int(input('Enter age of friend 2:'))
    age_3 = int(input('Enter age of friend 3:'))
    age_4 = int(input('Enter age of friend 4:'))
    age_5 = int(input('Enter age of friend 5:'))
    # Sum ages
    sum_of_ages = age_1 + age_2 + age_3 + age_4 + age_5
    # Average the ages
    results = sum_of_ages / 5
    # Print the results
    print('Average age:', results)

# Line which calls the above function.
average_age()