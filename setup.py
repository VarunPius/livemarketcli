from setuptools import setup

setup(
    name='LiveMarketTrackerCLI',
    version="1.0",
    author="Varun Pius Rodrigues",
    description="CLI Application to track stock market prices on command line",
    url="https://github.com/VarunPius/livemarketcli",
    install_requires=['requests','urwid'],
    packages=['lib'],
    entry_points={
        'console_scripts':['mktcli=run:main']
    },
)
