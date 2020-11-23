# src/hypermodern_python/console_rest_wikipedia.py
import textwrap # to wrap lines when printing text to the console

import click
import requests

from . import __version__


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL) as response: # sends an HTTP GET request 
        # check the HTTP status code and raise an exception if it signals an error
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]
    
    #  specify the foreground color
    click.secho(title, fg="green")      
    # wraps the text in extract so that every line is 
    # at most 70 characters long(which is the default)
    click.echo(textwrap.fill(extract))