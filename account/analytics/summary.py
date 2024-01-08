import csv
import keyFunctions
from account import start

def get_budget_summary(username, csv=True):
    filename = keyFunctions.get_budget_csv(username)
    if csv:
        get_summary(filename)
        
    
    
    start.welcome(username, True)
    

def get_summary(filename):
    try:
        data ={
            '0': 0,
            '1': 0,
            '2': 0,
            3: 0
        }
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row[2], row[3], [4])
                    
        return data
    
    except:
        return None