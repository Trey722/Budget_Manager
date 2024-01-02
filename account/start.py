import click
from account import add 



def list_commands():
    print("Your avivable commanns are.")
    print(" --add \n    Which allows you to add something to your budget")




    
def welcome(username):
    print(f"Hello, {username}")
    command = click.prompt("Please eneter what you would like to do ->")
    
    if command == "--help":
        return list_commands()
    
    if command[0:4] == "--add":
        
    
    
welcome("bob123")
    




