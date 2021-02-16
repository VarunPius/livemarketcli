import urwid
#import lib.tracker as tracker

palette = [
    ('titlebar', 'dark red', ''),
    ('refresh button', 'dark green,bold', ''),
    ('quit button', 'dark red', ''),
    ('getting quote', 'dark blue', ''),
    ('headers', 'white,bold', ''),
    ('change ', 'dark green', ''),
    ('change negative', 'dark red', '')]


def basic_display(price_dict):
    for ticker, price in price_dict.items():
        print(ticker, price['regularMarketPrice'])

def cli_ui():
    for ticker, price in price_dict.items():
        display_str = "Share: " + ticker + "  | price: " + str(price)
        txt = urwid.Text(display_str)
        fill = urwid.Filler(txt, 'top')
        loop = urwid.MainLoop(fill)
    #tracker.track_market()
    loop.run()

def main(price_dict):
    basic_display(price_dict)
"""
TICKER | PRICE | CHANGE | % CHANGE |
"""
