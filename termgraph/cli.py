"""CLI entry point."""
import sys
import click
from termgraph.charts import bar_chart, sparkline
from termgraph.parser import parse_input

@click.group()
def main():
    """Beautiful charts in your terminal."""
    pass

@main.command()
@click.argument("source", default="-")
@click.option("--color/--no-color", default=True)
@click.option("--width", default=40, help="Chart width")
def bar(source, color, width):
    """Draw a bar chart."""
    data = parse_input(source)
    output = bar_chart(data, width=width, color=color)
    click.echo(output)

@main.command()
@click.argument("source", default="-")
def spark(source):
    """Draw a sparkline."""
    data = parse_input(source)
    output = sparkline([v for _, v in data])
    click.echo(output)
