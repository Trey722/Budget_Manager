import click
import keyFunctions


# Type = 1 for add 0 for subtract
# Amount
# catogery such as luxury 
# descritpiton
def add_something(username : str, type : int, amount : float, catogery : str, date, descirption : str = None, instiution : str = None):
    csv_location = f"data/{username}/budget.csv"
    keyFunctions.add_line_to_csv(csv_location, [username, type, amount, catogery, date, descirption, instiution])
    
# 0 means confired
# 1 means retyr
def confirm_input(input):
    user_choice = click.prompt(
        f"Are you sure you want to input {input}. Enter Y or N",
        type=click.STRING,
        default=0,
        show_default=False
    )
    
    if ("Y" in user_choice):
        return 0
    elif "N" in user_choice:
        return 1
    else:
        click.echo("Could not understand user input")
        confirm_input(input)
    
    return user_choice
    
    
    
def get_type() -> int:
    user_choice = click.prompt(
        "Would you like to (1) add income (2) add expense Enter 1 or 2: ",
        type=int,
        default=0,
        show_default=False
    )
    
    if user_choice == 1:
        return 1
    
    elif user_choice == 2:
        return 0 
    else:
        click.echo("Could not understand")
        get_type()
        
        
def get_string(request, deafult=None):
    user_stirng = click.prompt(request, type=click.STRING, default=deafult)
    if (user_stirng == 'None'): return None
    return user_stirng


def get_category():
    return get_string("Please eneter the catgoery you would like to associate this with")
        
        

        
        
def get_amount(type) -> int:
    user_choice = click.prompt(
        "Please enter the amount of money this transaction was ",
        type=int,
        default=0,
        show_default=False
    )
    
    if type == 1:
        if user_choice < 0:
            if (confirm_input(user_choice)) == 0:
                return user_choice
            else:
                return get_amount()
                
        else:
            return user_choice 
        
    elif type == 0:
        if user_choice > 0:
            if (confirm_input(user_choice)) == 0:
                return user_choice
            else:
                return get_amount()   
        else:
            return user_choice 
        
        


    
        
        
def get_date():
    user_date = click.prompt(
        "Please enter the date in YYYY-MM-DD ",
        type=click.STRING,
        default=0,
        show_default=False
    )
    

    if user_date[4] != "-" or user_date[7] != "-":
        click.echo("can't find hypens")
        click.echo("Please enter the date in YYYY-MM-DD. For exmaple, 2024-01-02")
        return get_date()
    
    try:
        year = int(user_date[:4])
        month = int(user_date[4:6])
        day = int(user_date[6])
        return user_date
    except:
        click.echo("Can't find numbers")
        click.echo("Please enter the ate using YYYY-MM-DD form. For exmaple, 2024-01-02")
        return get_date()
            
    
def add_prompt(username):
    new_item = {}
    
    new_item['username'] = username
    new_item['type'] = get_type()
    new_item['amount'] = get_amount(new_item['type'])
    new_item['catagoery'] = get_string("Please enter the catgoery you would like to asssociate this with")
    new_item['date'] = get_date()
    new_item['description'] = get_string("Please eneter an option descirtion")
    new_item['instiution'] = get_string("Please enter the instiatuion you would like to asssociate this with")
    
    add_something(new_item['username'], new_item['type'], new_item['amount'], new_item['catagoery'], new_item['date'], new_item['description'], new_item['instiution'])
    
    

    
    



    
    