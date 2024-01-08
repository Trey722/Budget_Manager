import click
from account import add, create_budget
from account.analytics import budget_anyaltics, budget_goal_anyaltics, compare


def list_commands(username):
    print("Your avivable commanns are.")
    print(" --add \n    Which allows you to add something to your budget")
    print(" --creae buget goal \n    Which allows you to create a buget goal")
    welcome(username, True)



def welcome(username, repeat=False):
    if repeat == False:
        print(f"Hello, {username}")
        
    command = click.prompt("Please enter what you would like to do ->")
    
    command = command.replace(' ', '')
    if command == "--help":
        return list_commands(username)
    
    
    if command[:5] == "--add":
        add.add_prompt(username)
        
    elif command[:17] == "--createbudgetgoal":
        create_budget.create_budget_goal()
        
    elif command == "--checkbudget":
        return False
    
    elif command == "--analyticsbudget":
        budget_anyaltics.get_budget_anyaltics(username, True)
        
    elif command == '--analyticsbudgetgoal':
        budget_goal_anyaltics.get_budget_anyaltics_goal(username)
        
    elif command == '--analyticsbudgetgoal-budget':
        print("starting")
        compare.compare_goal_start(username)
       
        
        
    welcome(username, True)

