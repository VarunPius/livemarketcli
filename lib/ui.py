#####################################################################
# Author      : Varun Pius Rodrigues                               ##
# File        : ui.py                                              ##
# Description : Implementation to print values                     ##
#####################################################################

# External Packages
import urwid

# Project Packages:
import lib.tracker as tracker

################################################################################
# Basic implementation to display Current Price
################################################################################

def basic_display(price_dict):
    for ticker, price in price_dict.items():
        print(ticker, price['regularMarketPrice'])


################################################################################
# UI implementation
################################################################################

ticker = []

def set_ticker(arg_ticker):
    global ticker
    ticker = arg_ticker

def get_ticker():
    return ticker

template = [
    ('titlebar', 'dark red', ''),
    ('refresh button', 'dark green,bold', ''),
    ('quit button', 'dark red', ''),
    ('getting quote', 'dark blue', ''),
    ('headers', 'white,bold', ''),
    ('num ', 'dark green', ''),
    ('num negative', 'dark red', '')]

# Header
header_txt = urwid.Text(' Stock Quotes')
header = urwid.AttrMap(header_txt, 'titlebar')

# Footer
footer_txt = urwid.Text([
    'Press (', ('refresh button', 'R'), ') to manually refresh.',
    'Press (', ('quit button', 'Q'), ') to quit.'
])

# Body
quote_text = urwid.Text('Refresh to get quote!')
quote_filler = urwid.Filler(quote_text, valign='top', top=1, bottom=1)
v_padding = urwid.Padding(quote_filler, left=1, right=1)
quote_box = urwid.LineBox(v_padding)

# Layout
layout = urwid.Frame(header=header, body=quote_box, footer=footer_txt)


def format_positive_number(num):
    if not num:
        return "0"
    else:
        return "+{}".format(num) if num >= 0 else str(num)

def get_color(num):
    num_color = "num "
    if num < 0:
        num_color += "negative"
    return num_color

def append_list(lst, st, tabsize=10, color='white'):
    lst.append((color, st.expandtabs(tabsize)))


def format_data():
    ticker = get_ticker()
    price_dict = tracker.track_market(ticker)
    updates = [
        ('headers', 'Stock \t '.expandtabs(10)),
        ('headers', 'Last Price \t '.expandtabs(5)),
        ('headers', 'Change \t '.expandtabs(15)),
        ('headers', '% Change \t \n'.expandtabs(10))]
        #('headers', 'Gain \t '.expandtabs(10)),
        #('headers', '% Gain \t \n'.expandtabs(8)) ]

    for ticker, price in price_dict.items():
        mkt_price = price['current_price']
        mkt_change = price['current_change']
        mkt_change_pct = price['current_change_percent']
        #print(mkt_price, mkt_change, mkt_change_pct)

        append_list(updates, "{} \t".format(ticker), tabsize=11)
        append_list(updates, "{} \t".format(str(mkt_price)), tabsize=16)
        append_list(updates, "{} \t".format(format_positive_number(mkt_change)), tabsize=8, color=get_color(mkt_change))
        append_list(updates, "{} \t \n".format(format_positive_number(mkt_change_pct)), tabsize=1, color=get_color(mkt_change_pct))

    return updates


def refresh_or_exit(key):
    if key in ('r', 'R'):
        ticker = get_ticker()
        refresh(main_loop, "")
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


def refresh(_loop, _data):
    main_loop.draw_screen()
    quote_box.base_widget.set_text(format_data())
    main_loop.set_alarm_in(15, refresh)


main_loop = urwid.MainLoop(layout, template, unhandled_input=refresh_or_exit)


def cli_ui(ticker):
    main_loop.set_alarm_in(0, refresh)
    main_loop.run()


def main(ticker):
    #price_dict = tracker.track_market(ticker)
    #basic_display(price_dict)

    set_ticker(ticker)
    cli_ui(ticker)


################################################################################
# Rough
################################################################################

"""
TICKER | PRICE | CHANGE | % CHANGE |
"""

"""
def cli_ui(ticker):
    txt = urwid.Text("Hello")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    #tracker.track_market()
    loop.run()
"""

"""
{
    "Global Quote": {
        "01. symbol": "IBM",
        "02. open": "121.0000",
        "03. high": "121.3600",
        "04. low": "120.0900",
        "05. price": "120.8000",
        "06. volume": "3871195",
        "07. latest trading day": "2021-02-12",
        "08. previous close": "120.9100",
        "09. change": "-0.1100",
        "10. change percent": "-0.0910%"
    }
}
"""

"""
        price_dict[ticker]['regularMarketPreviousClose'] = stock_data['regularMarketPreviousClose']
        price_dict[ticker]['regularMarketOpen'] = stock_data['regularMarketOpen']
        price_dict[ticker]['regularMarketPrice'] = stock_data['regularMarketPrice']
        price_dict[ticker]['regularMarketTime'] = stock_data['regularMarketTime']
        price_dict[ticker]['regularMarketChange'] = stock_data['regularMarketChange']
        price_dict[ticker]['regularMarketChangePercent'] = stock_data['regularMarketChangePercent']
        price_dict[ticker]['regularMarketDayHigh'] = stock_data['regularMarketDayHigh']
        price_dict[ticker]['regularMarketDayLow'] = stock_data['regularMarketDayLow']
        price_dict[ticker]['postMarketPrice'] = stock_data['postMarketPrice']
        price_dict[ticker]['postMarketChange'] = stock_data['postMarketChange']
        price_dict[ticker]['postMarketChangePercent'] = stock_data['postMarketChangePercent']
        price_dict[ticker]['marketState'] = stock_data['postMarketChangePercent']

"""
