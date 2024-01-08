import keyFunctions
import csv
from account import start

def get_budget_anyaltics_goal(username, csv=True):
    filename = keyFunctions.get_bugdet_goal_csv(username)
    if csv:
        data = get_breakdown_csv_goal(filename)
        
    get_percent_breakdown_goal(data)
    
    start.welcome(username, True)
    

def get_breakdown_csv_goal(filename):
    data ={
        '0': 0,
        '1': 0,
        '2': 0,
        3: 0
    }
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            cur = str(row[2])
            try:
                data[cur] += float(row[1])
            except:
                data[3] += 1
                
    return data

def get_percent_breakdown_goal(breakdown_dict, prints=True):
    income = breakdown_dict['0']
    needs = breakdown_dict['2']
    wants = breakdown_dict['1']
    savings = breakdown_dict['0'] + needs + wants
    
   
        
    if prints:
        if income == 0:
            print(f"Budget Breakdown \n Income | ${income}\n  Needs | ${needs}\n  Wants | ${wants}\n  total Spending | ${wants + needs}\n  Saving | ${savings}\n ")
        else:
            print(f"Budget Breakdown \n Income | ${income} | 100% \n  Needs | ${needs} | {abs(needs/income * 100)} \n  Wants | ${wants} | {wants/income * 100}% \n  total Spending | ${wants + needs} | {abs((wants + needs) / income * 100)}% \n  Saving | ${savings} |{abs(savings/income * 100)}% \n ")
        
    return income, needs, wants, savings
    