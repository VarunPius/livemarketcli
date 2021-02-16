# Live Market CLI
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/badge/version-2.1.1-blue)

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
![Demo](docs/ScreenShot.png?raw=true "Demo")

# Credits
I took a lot of help for the `urwid` implementation from Boa Ho Man (https://github.com/aranair). His `rtscli - Realtime Stock Ticker CLI` repository (https://github.com/aranair/rtscli) is worth having a look. I took parts of the template from that application for how the application looks and feels.
