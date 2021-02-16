# Live Market CLI
<a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a> <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>

This application is to track live stock market prices from the convenience of a command line. This makes it easier to keep track of some stocks in your watchlist live rather than having to refresh your browser over and over again.

# Installation
Clone the repo or download the source and then run the following:
```
pip install .
```
or
```
Python setup.py install
```

# Running the application
Once the application is installed, you can run it as follows:
```
mktcli
```
`mktcli` provides `ticker` option to add stock tickers of your choice. We do this as follows:
```
mktcli -t <stock_ticker1> <stock_ticker2>
```
For example:
```
mktcli -t AAPL MSFT TWTR
```
By default, it would return values for `$VOO` and `$VTI`

# Screenshot
![Demo](https://github.com/VarunPius/livemarketcli/blob/master/docs/ScreenShot.png?raw=true "Demo")

# Credits
I took a lot of help for the `urwid` implementation from Boa Ho Man (https://github.com/aranair). His `rtscli - Realtime Stock Ticker CLI` repository (https://github.com/aranair/rtscli) is worth having a look. I took parts of the template from that application for how the application looks and feels.
