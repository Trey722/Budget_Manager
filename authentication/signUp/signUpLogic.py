import click
from authentication import auth, csvManage
from authentication.signUp.specialCharcters import special_charcters

from keyFunctions import get_csv_location

import account.start as start

global username

def create_account_logic():
    global username
    username = get_username()
    password = get_password()
    auth.createAccount(username=username, password=password)
    start.welcome(username)

def get_username():
    global username
    username = click.prompt("Enter Username", type=click.STRING)
    if (check_username(username=username) == False):
        get_username()
    else:
        return username

def get_password():
    password1 = auth.hash_password(click.prompt("Enter Password", type=click.STRING, hide_input=True))
    password2 = auth.hash_password(click.prompt("Reeneter Password", type=click.STRING, hide_input=True))
    
    if (password1 == password2):
        return password1
    else:
        click.echo("Passwors did not equal. Try again")
        get_password()


def check_username(username):
    dict = csvManage.csv_to_dict(get_csv_location("auth.csv"))
    if (dict.get(username) != None):
        click.echo("username already exists")
        return False
    SP = special_charcters 
    for i in SP:
        if i in username:
            click.echo("A special charcter is contained wihen the function")
            click.echo(f"remeber the following are special charcters {SP}")
            return False
    return True
   
    
    
    
    