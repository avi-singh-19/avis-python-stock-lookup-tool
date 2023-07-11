import pytest
import yfinance as yf
import pandas as pd


@pytest.fixture
def valid_yf_api_call():
    return pd.DataFrame(yf.download(tickers='AAPL', period='1d', interval='2m'))


@pytest.fixture
def invalid_yf_api_call():
    return pd.DataFrame(yf.download(tickers='Apple', period='1d', interval='2m'))


@pytest.fixture
def matching_yf_api_ticker():
    return 'AAPL'
