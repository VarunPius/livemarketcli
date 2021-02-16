# API Resources
These are some of the resources we can use for Market data.
- AlphaVantage
- Interactive Brokers (IBKR): https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/
- IEX
- Polygon (polygon.io)
- Alpaca
- Yahoo Finance:
    - `yfinance` is a popular library for Python (https://github.com/ranaroussi/yfinance);
    - `YahooFinancials` is another alternative would be YahooFinancials (https://github.com/JECSand/yahoofinancials)
- Finnhub (finnhub.io)
- Quandl
- Currencylayer API
- Traider API
- World trading data (https://www.worldtradingdata.com/)
- Marketstack
- QuantConnect

## Yahoo API
The biggest advantage of using Yahoo API is it's free (no registration required) and easy to use. I didn't use `yfinance` for this project. Instead I used the underlying link that `yfinance` and other projects use, viz. `query1.yahoo.com`. This is the link to Yahoo Query Language, from where data is retrieved.

An amazing answer from StackOverflow helped me solve one of this problem (https://stackoverflow.com/a/47505102) of how to retrieve data. Here is the solution.
Yahoo has gone to a Reactjs front end which means if you analyze the request headers from the client to the backend you can get the actual JSON they use to populate the client side stores.

### Hosts:
- `query1.finance.yahoo.com` HTTP/1.0
- `query2.finance.yahoo.com` HTTP/1.1 (difference between HTTP/1.0 & HTTP/1.1 explained below)

If you plan to use a proxy or persistent connections use `query2.finance.yahoo.com`. But for the purposes of this post, the host used for the example URLs is not meant to imply anything about the path it's being used with.

### Fundamental Data
(substitute your symbol for: AAPL)

- `/v10/finance/quoteSummary/AAPL?modules=`
**Inputs for the ?modules= query**:
```
    [
       'assetProfile',
       'summaryProfile',
       'summaryDetail',
       'esgScores',
       'price',
       'incomeStatementHistory',
       'incomeStatementHistoryQuarterly',
       'balanceSheetHistory',
       'balanceSheetHistoryQuarterly',
       'cashflowStatementHistory',
       'cashflowStatementHistoryQuarterly',
       'defaultKeyStatistics',
       'financialData',
       'calendarEvents',
       'secFilings',
       'recommendationTrend',
       'upgradeDowngradeHistory',
       'institutionOwnership',
       'fundOwnership',
       'majorDirectHolders',
       'majorHoldersBreakdown',
       'insiderTransactions',
       'insiderHolders',
       'netSharePurchaseActivity',
       'earnings',
       'earningsHistory',
       'earningsTrend',
       'industryTrend',
       'indexTrend',
       'sectorTrend']
```
**Example URL**: querying for all of the above modules
- `https://query2.finance.yahoo.com/v10/finance/quoteSummary/AAPL?modules=assetProfile%2CsummaryProfile%2CsummaryDetail%2CesgScores%2Cprice%2CincomeStatementHistory%2CincomeStatementHistoryQuarterly%2CbalanceSheetHistory%2CbalanceSheetHistoryQuarterly%2CcashflowStatementHistory%2CcashflowStatementHistoryQuarterly%2CdefaultKeyStatistics%2CfinancialData%2CcalendarEvents%2CsecFilings%2CrecommendationTrend%2CupgradeDowngradeHistory%2CinstitutionOwnership%2CfundOwnership%2CmajorDirectHolders%2CmajorHoldersBreakdown%2CinsiderTransactions%2CinsiderHolders%2CnetSharePurchaseActivity%2Cearnings%2CearningsHistory%2CearningsTrend%2CindustryTrend%2CindexTrend%2CsectorTrend`

The `%2C` is the Hex representation of `,` and needs to be inserted between each module you request. details about the hex encoding bit(if you care: https://stackoverflow.com/questions/6182356/what-is-2c-in-a-url)

### Options contracts
- `/v7/finance/options/AAPL` (current expiration)
- `/v7/finance/options/AAPL?date=1679011200` (March 17, 2023 expiration)

**Example URL**:
- `https://query2.yahoo.finance.com/v7/finance/options/AAPL` (current expiration)
- `https://query2.yahoo.finance.com/v7/finance/options/AAPL?date=1679011200` (Match 17, 2023 expiration)

Any valid future expiration represented as a UNIX timestamp can be used in the `?date=` query. If you query for the current expiration the JSON response will contain a list of all the valid expirations that can be used in the `?date=` query. (Here is a post explaining converting human-readable dates to UNIX timestamp in Python: https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date)

### Price
- `/v8/finance/chart/AAPL?symbol=AAPL&period1=0&period2=9999999999&interval=3mo`

Possible inputs for &interval=: 1m, 5m, 15m, 30m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

    m (minute) intervals are limited to 30days with period1 and period2 spaning a maximum of 7 days per/request. Exceeding either of these limits will result in an error and will not round

    h (hour) interval is limited to 730days with no limit to span. Exceeding this will result in an error and will not round

`period1=`: UNIX timestamp representation of the date you wish to start at.

    d (day), wk (week), mo (month) intervals with values less than the initial trading date will be rounded up to the initial trading date.

`period2=`: UNIX timestamp representation of the date you wish to end at.

    For all intervals: values greater than the last trading date will be rounded down to the most recent timestamp available.

**Add pre & post market data** : `&includePrePost=true`

**Add dividends & splits** : `&events=div%7Csplit`
`%7C` is hex for `|`. `,` will work but internally Yahoo uses pipe

**Example URL**:
- `https://query1.finance.yahoo.com/v8/finance/chart/AAPL?symbol=AAPL&period1=0&period2=9999999999&interval=1d&includePrePost=true&events=div%7Csplit`

The above request will return all price data for ticker AAPL on a 1-day interval including pre and post-market data as well as dividends and splits.

Note: the values used in the price example URL for `period1=` & `period2=` are to demonstrate the respective rounding behavior of each input.`

## HTTP 1.0 vs HTTP 1.1
### Proxy support and the Host field:

HTTP 1.1 has a required Host header by spec.

HTTP 1.0 does not officially require a Host header, but it doesn't hurt to add one, and many applications (proxies) expect to see the Host header regardless of the protocol version.

Example:
```
GET / HTTP/1.1
Host: www.blahblahblahblah.com
```
This header is useful because it allows you to route a message through proxy servers, and also because your web server can distinguish between different sites on the same server.

So this means if you have blahblahlbah.com and helohelohelo.com both pointing to the same IP. Your web server can use the Host field to distinguish which site the client machine wants.

### Persistent connections:

HTTP 1.1 also allows you to have persistent connections which means that you can have more than one request/response on the same HTTP connection.

In HTTP 1.0 you had to open a new connection for each request/response pair. And after each response the connection would be closed. This lead to some big efficiency problems because of TCP Slow Start.

### OPTIONS method:

HTTP/1.1 introduces the OPTIONS method. An HTTP client can use this method to determine the abilities of the HTTP server. It's mostly used for Cross Origin Resource Sharing in web applications.

### Caching:

HTTP 1.0 had support for caching via the header: If-Modified-Since.

HTTP 1.1 expands on the caching support a lot by using something called 'entity tag'. If 2 resources are the same, then they will have the same entity tags.

HTTP 1.1 also adds the If-Unmodified-Since, If-Match, If-None-Match conditional headers.

There are also further additions relating to caching like the Cache-Control header.

### 100 Continue status:

There is a new return code in HTTP/1.1 100 Continue. This is to prevent a client from sending a large request when that client is not even sure if the server can process the request, or is authorized to process the request. In this case the client sends only the headers, and the server will tell the client 100 Continue, go ahead with the body.

### Much more:
- Digest authentication and proxy authentication
- Extra new status codes
- Chunked transfer encoding
- Connection header
- Enhanced compression support

And Much much more.


# Python Learning
## Versioning Schemes
There are two types of versioning schemes:
- Internal version number: This can be incremented many times in a day (e.g. revision control number)
- Released version: This changes less often (e.g. semantic versioning)

People use different schemes as per their need, but semantic versioning is fairly widely used and authored by Tom Preston-Werner, co-founder of GitHub.

### Semantic Versioning
Semantic versioning follows the pattern of X.Y.Z
Or more readable would be [major].[minor].[patch]-[build/beta/rc]

E.g. `1.2.0-beta`
- major or X can be incremented if there are major changes in software, like backward-incompatible API release.
- minor or Y is incremented if backward compatible APIs are introduced.
- patch or Z is incremented after a bug fix.

How do we achieve this using Git?
By using tags:
Tags in Git can be used to add a version number.
```
git tag -a "v1.5.0-beta" -m "version v1.5.0-beta"
```
adds a version tag of v1.5.0-beta to your current Git repository. Every new commit after this will auto-increment tag by appending commit number and commit hash. This can be viewed using the git describe command.

`v1.5.0-beta-1-g0c4f33f` here `-1-` is the commit number and `0c4f33f` the abbreviation of commit's hash. The `g` prefix stands for "git".

Complete details can be viewed using:
```
git show v1.5.0-beta
```

## Handling for multiple Python versions
```
import urwid
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
try:
    # For Python3.0 and later
    from html.parser import HTMLParser
except ImportError:
    # Fall back to Python 2's HTMLparser
    from HTMLparser import HTMLparser
from simplejson import loads
from time import sleep
```
