#!/usr/bin/env python3

#sets beginning of the response
message = 'Looks like you earned '

# prompt user for their grade
user = input("What percentage did you receive on your exam?")

grade = int(user)
grade = round(grade)
# check values to respond with letter grade earned
if grade >= 90:
    message = message + 'an A. Excellent Work!'
elif grade >= 80:
    message = message + 'a B. Good Job'
elif grade >= 70:
    message = message + 'a C, you are an Average Joe'
elif grade >= 60:
    message = message + 'a D.  Better Luck Next Time.'
else:
    message = 'You FAILED!!'
print(message)
