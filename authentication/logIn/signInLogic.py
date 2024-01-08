import click
from authentication.auth import hash_password
from authentication import csvManage
import account.start as start
import keyFunctions

global username

def checkLogIn(username, password):
    usernamesandpassword = csvManage.csv_to_dict(keyFunctions.get_csv_location("auth.csv"))
    if (password + "\n" == usernamesandpassword.get(username)):
        return True
    else:
        return False
    
    
    


def sign_in_logic():
    global username
    username = click.prompt("Enter username", type=click.STRING)
    password = hash_password(click.prompt("Enter password", type=click.STRING, hide_input=True))
    if checkLogIn(username=username, password=password) == False:
        click.echo("Log in failed. username or password was incorrect")
        sign_in_logic()
    else:
        click.echo(f"Sign in was sucesful to {username}")
        start.welcome(username)
        
    