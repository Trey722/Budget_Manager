import click


def get_float_negative(text):
    return get_float(text) * -1

def get_float(text):
    number = click.prompt(text + "->", type=click.FLOAT)
    return number


def get_int(text):
    number = click.prompt(text + "->", type=click.INT)
    return number

