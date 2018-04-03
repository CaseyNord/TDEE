#################################################
# TDEE_Calculator.py
# Author:   Casey Nord/Kira Nesser
# Date Created: Feb 21, 2018
# Description: Calculator for BMR and TDEE
#################################################

def get_valid_int(maximum, prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That is not a valid input")
            continue

        if value > maximum:
            print("Enter a number between 1 and {}".format(maximum))
        elif value < 1:
            print("Enter a number between 1 and {}".format(maximum))
        else:
            break
    return value


def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("That is not a valid input")
            continue
    return value


print("How are you going to input your data?\n")
measurements = get_valid_int(2, "Enter 1 for Imperial, or 2 for Metric: ")

if measurements == 1:
    height = get_valid_float("Enter height in inches: ")
    weight = get_valid_float("Enter weight in lbs: ")
    weight = weight / 2.2
    height = height / 0.393701
elif measurements == 2:
    height = get_valid_float("Enter height in centimeters: ")
    weight = get_valid_float("Enter weight in kilograms: ")

age = get_valid_int(130, "Enter age: ")
gender = get_valid_int(2, "Enter 1 for male, or 2 for female: ")
activity_level = get_valid_int(5, "Enter 1 for sedentary, 2 for lightly active, " + 
                               "3 for moderately active, 4 for very active, " +
                               "or 5 for extra active: ")

if gender == 1:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
elif gender == 2:
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

print("BMR is: {}".format(int(round(bmr,0))))

if activity_level == 1:
    tdee = bmr * 1.2
elif activity_level == 2:
    tdee = bmr * 1.375
elif activity_level == 3:
    tdee = bmr * 1.55
elif activity_level == 4:
    tdee = bmr * 1.725
elif activity_level == 5:
    tdee = bmr * 1.9

print("TDEE is: {}".format(int(round(tdee,0))))