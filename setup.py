from setuptools import setup

setup(
    name='LiveMarketCLITracker',
    version="0.1",
    author="Varun Pius Rodrigues",
    description="Application to track stock market prices on command line",
    url="https://github.com/VarunPius/livemarketcli",
    install_requires=['Click', 'requests',],
    packages=['tracker'],
    entry_points='''
        [console_scripts]
        mktcli=run:main
    ''',
)
