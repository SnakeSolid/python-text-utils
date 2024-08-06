#!/usr/bin/env python3

import click
from textutils.paragraph import convert as paragraph_convert
from textutils.shorten import convert as shorten_convert
from textutils.subtitles import convert as subtitles_convert
from textutils.translate import convert as translate_convert
import sys

LANGUAGES = [
    "English",
    "Russian",
    "German",
    "French",
    "Spanish",
    "Polish",
    "Greek",
    "Hebrew",
    "Arabic",
    "Hindi",
    "Chinese",
    "Japanese",
]


@click.group()
def cli():
    """Text utilities."""
    pass


@cli.command()
@click.option("-o", "--output", help="Output file (default STDOUT)")
@click.argument("path")
def convert(path, output):
    if output is None:
        subtitles_convert(path, sys.stdout)
    else:
        with open(output, "w") as f:
            subtitles_convert(path, f)


@cli.command()
@click.option("-o", "--output", help="Output file (default STDOUT)")
@click.option("-s",
              "--min-lines",
              default=10,
              help="Minimal number of line in paragraph",
              type=int,
              show_default=True)
@click.option("-x",
              "--max-lines",
              default=20,
              help="Maximal number of line in paragraph",
              type=int,
              show_default=True)
@click.argument("path")
def paragraph(path, output, min_lines, max_lines):
    if output is None:
        paragraph_convert(path, sys.stdout, min_lines, max_lines)
    else:
        with open(output, "w") as f:
            paragraph_convert(path, f, min_lines, max_lines)


@cli.command()
@click.option("-o", "--output", help="Output file (default STDOUT)")
@click.option("-f",
              "--factor",
              default=5,
              help="Number of paragraphs to shorten to one",
              type=int,
              show_default=True)
@click.option("-l",
              "--language",
              default="English",
              help="Destination language",
              show_default=True,
              type=click.Choice(LANGUAGES, case_sensitive=False))
@click.option("-m",
              "--model",
              default="gemma2",
              help="LLM used to shorten text",
              show_default=True)
@click.option("--progress/--no-progress",
              default=True,
              help="Show progress bar",
              show_default=True)
@click.argument("path")
def shorten(path, output, factor, language, model, progress):
    if output is None:
        shorten_convert(path, sys.stdout, factor, language, model, progress)
    else:
        with open(output, "w") as f:
            shorten_convert(path, f, factor, language, model, progress)


@cli.command()
@click.option("-o", "--output", help="Output file (default STDOUT)")
@click.option("-m",
              "--model",
              default="gemma2",
              help="LLM used to shorten text",
              show_default=True)
@click.option("-l",
              "--language",
              default="Russian",
              help="Destination language",
              show_default=True,
              type=click.Choice(LANGUAGES, case_sensitive=False))
@click.option("--progress/--no-progress",
              default=True,
              help="Show progress bar",
              show_default=True)
@click.argument("path")
def translate(path, output, model, language, progress):
    if output is None:
        translate_convert(path, sys.stdout, model, language, progress)
    else:
        with open(output, "w") as f:
            translate_convert(path, f, model, language, progress)


if __name__ == "__main__":
    cli()
