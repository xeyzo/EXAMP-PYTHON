import click
from src.Current_weather import weather


@click.group()
def cli():
    pass


cli.add_command(weather)


if __name__ == "__main__":
    cli()