import click






    
    

@click.command()
def user_interaction():
    """Asks the user to sign in or create an account"""
    click.echo("If you want to quit. Hit control C at any time unless speicifed not to")
    user_choice = click.prompt(
        "Would you like to (1) Sign In or (2) Create an Account? Enter 1 or 2: ",
        type=int,
        default=0,
        show_default=False
    )

    if user_choice == 1:
        
        from authentication.logIn.signInLogic import sign_in_logic
        sign_in_logic()
        
    elif user_choice == 2:
        from authentication.signUp.signUpLogic import create_account_logic
        create_account_logic()
       
    else:
        click.echo("Invalid choice. Please enter either 1 or 2.")
        user_interaction()

if __name__ == '__main__':
    user_interaction()


    
    
    
    
    
    
    
    

