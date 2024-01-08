import click 
from general import get_float_negative, get_float, get_int
import csv

def create_budget_goal(username):
    budget = get_budget()

    # Write breakdown to CSV
    with open(f"data/{username}_budget_breakdown.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Amount', 'Type'])  # Writing headers

        # Writing income
        for job, amount in budget['income'].items():
            writer.writerow([job, amount, 0])
        writer.writerow(['Other sources', budget['income']['other'], 0])

        # Writing needs
        for category, amount in budget['needs'].items():
            writer.writerow([category, amount, 2])

        # Writing wants
        for category, amount in budget['wants'].items():
            writer.writerow([category, amount, 1])

    print(f"Budget breakdown for {username} saved to {username}_budget_breakdown.csv")

    return budget
    

def get_budget():
    budget = {}
    
    budget['income'] = get_income()
    budget['needs'] = get_budget_needs()
    budget['wants'] = get_budget_wants()
    
    return budget


def get_income():
    budget_income = {}
    x = get_int("Please enter the amount of jobs you have")
    for i in range(x):
        budget_income[f'job{i}'] = get_int(f"Please enter the amount you make from job {x}")
    budget_income['other'] = get_float("Please enter the amount you make from other sources")
    
    return budget_income

def get_budget_needs():
    budget_needs = {}
    budget_needs['housing'] = get_float_negative("Please enter the amount you pay for your mortgage or rent")
    budget_needs['housingExpenses'] = get_float_negative("Please enter the amount you pay for housing expenses")
    budget_needs['houseTax'] = get_float_negative("Please enter the amount you pay in property taxes")
    budget_needs['autoInsurance'] = get_float_negative("Please enter how much you pay in auto insurance")
    budget_needs['autoPayment'] = get_float_negative("Please enter your car payment")
    budget_needs['autoParking'] = get_float_negative("Please enter the amount you pay for parking")
    budget_needs['autoMaintenance'] = get_float_negative("Please enter the amount you pay to maintain the car")  
    budget_needs['gas'] = get_float_negative("Please enter the amount you pay for gas")
    budget_needs['healthInsurance'] = get_float_negative("Please enter the amount you pay in premiums")
    budget_needs['healthExpenses'] = get_float_negative("Please enter the amount you pay out-of-pocket for health insurance")
    budget_needs['lifeInsurance'] = get_float_negative("Please enter the amount you pay in life insurance")
    budget_needs['power'] = get_float_negative("Please enter the amount you pay for electricity")
    budget_needs['water'] = get_float_negative("Please enter water bill")
    budget_needs['garbage'] = get_float_negative("Please enter the amount you pay for garbage")
    budget_needs['food'] = get_float_negative("Please enter the amount you pay for necessary groceries")
    budget_needs['publicTransportation'] = get_float_negative("Please enter the amount you pay for public transportation")
    budget_needs['phone'] = get_float_negative("Please enter your phone bill")
    budget_needs['internet'] = get_float_negative("Please enter the amount you pay for internet")
    budget_needs['loanPayments'] = get_float_negative("Please enter the amount you pay in non-house loans")
    budget_needs['alimony'] = get_float_negative("Please enter the amount of alimony payments you make")
    budget_needs['other'] = get_float_negative("Please enter the other necessities")
    
    return budget_needs

def get_budget_wants():
    budget_wants = {}
    budget_wants['diningOut'] = get_float_negative("Please enter the amount you spend dining out")
    budget_wants['specialMeals'] = get_float_negative("Please enter the amount you spend on expensive non necceaity food at home")
    budget_wants['travel'] = get_float_negative("Please enter the amount you spend on travel")
    budget_wants['gym'] = get_float_negative("Please enter the amount you spend at the gym or other fitness")
    budget_wants['homeDecor'] = get_float_negative("Please enter the amount you spen on decrations")
    budget_wants['cable/streaming'] = get_float_negative("Please enter the amount you spend on cable or streaming")
    budget_wants['enteirmaint'] = get_float_negative("Please enetr the amount you spend at movies, concerts or other enterianment")
    budget_wants['party'] = get_float_negative("Please enter the amount you spend at clubs, partying, and alchol")
    budget_wants['other'] = get_float_negative("Please enter the amount you spend on other non essential expenses")
    
    return budget_wants
    




   
    



    
    
    
    