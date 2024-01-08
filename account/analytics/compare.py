from account.analytics import budget_anyaltics, budget_goal_anyaltics
from account import start
import keyFunctions


def compare_goal_start(username):
    data_goal = budget_goal_anyaltics.get_breakdown_csv_goal(keyFunctions.get_bugdet_goal_csv(username))
    data_real = budget_anyaltics.get_breakdown_csv(keyFunctions.get_budget_csv(username))
    delta = {}
    
    print(data_goal['0'])
    delta['0'] = data_goal['0'] - data_real['1']
    delta['1'] = data_goal['1'] - data_real['1']
    delta['2'] = data_goal['2'] - data_real['2']
    
    print(f"income: {delta['0']} \n wants {delta['1']} \n needs {delta['2']}")
    
    start.welcome(username)
    
    