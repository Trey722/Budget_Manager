import click 



def welcome(username):
    click.echo(f"Welcome {username}")
    click.prompt("Please enetr a command")
    