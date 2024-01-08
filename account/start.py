import click
from account import add, create_budget
from account.analytics import budget_anyaltics, budget_goal_anyaltics, compare, summary


def list_commands(username):
    print("Your avivable commanns are.")
    print(" --add \n    Which allows you to add something to your budget")
    print(" --create buget goal \n    Which allows you to create a buget goal")
    print(" --budget summary \n    Gets a summary of all of your pruchases")
    print(" --analytics budget \n    Gets the data invovled in your budget")
    print(" --analytics budget goal - budget \n Gets how much you can spend in wants and needs to meet you goal and how much you need to earn to meet your income goal")
    print(" --analytics budget goal \n   Shows your goal budget")
    welcome(username, True)



def welcome(username, repeat=False):
    if repeat == False:
        print(f"Hello, {username}")
        
    command = click.prompt("Please enter what you would like to do ->")

    command = command.replace(' ', '')
    if command == "--help":
        return list_commands(username)
    
    print(command)
    
    if "--add" in command:
        add.add_prompt(username)
        
    elif "--createbudgetgoal" in command:
        create_budget.create_budget_goal()
        
    elif "--budgetsummary" in command:
        summary.get_budget_summary(username)
    
    elif  "--analyticsbudget" in command:
        budget_anyaltics.get_budget_anyaltics(username, True)
        
    elif '--analyticsbudgetgoal' in command:
        budget_goal_anyaltics.get_budget_anyaltics_goal(username)
        
    elif '--analyticsbudgetgoal-budget' in command == True:
        compare.compare_goal_start(username)
       
        
        
    welcome(username, True)

