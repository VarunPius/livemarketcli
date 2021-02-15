#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : run.py                                             ##
# Description : Main program                                       ##
#####################################################################

import argparse
import click

# Project Packages:
import lib.ui as ui
import lib.tracker as tracker


def main():
    arg_parser = argparse.ArgumentParser(description='List of stocks to track')
    arg_parser.add_argument('--ticker', '-t', help='Enter list of stocks', nargs='+', default=['VOO', 'VTI']) # nargs = + for variable arguments
    args = arg_parser.parse_args()
    ticker = args.ticker
    print(ticker)
    price_dict = tracker.track_market(ticker)
    print(price_dict)
    #ui.main(price_dict)
    #ui.main()


"""
@click.command()
@click.option(
    '--ticker',
    '-t',
    default='VOO,VTI',
    help='Enter list of stocks')
def main(ticker):
    print("Hello")
    print(ticker)
    """
