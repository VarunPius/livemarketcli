import urwid
import lib.tracker as tracker


def main(price_dict):
    txt = urwid.Text("Hello UI")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    tracker.track_market()
    loop.run()
