import os
import requests
from dotenv import load_dotenv
import yfinance as yf

load_dotenv()

API_KEY = os.getenv('ALPHA_API_KEY')

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TATASTEEL.nse&outputsize=full&apikey={API_KEY}$datatype=csv'

r = requests.get(url)
data = r.json()
print(data)

ticker = 'TATASTEEL.NS'
data = yf.download(ticker, start='2000-01-01', end='2024-05-29')
print(data)
data.to_csv(f'{ticker}.csv')

stock = yf.Ticker(ticker)
financials = stock.financials
print(financials)

msft = yf.Ticker(ticker)
msft.info

msft.income_stmt
msft.quarterly_income_stmt
msft.balance_sheet
msft.cashflow
msft.major_holders
msft.institutional_holders
msft.recommendations
msft.recommendations_summary
msft.upgrades_downgrades
msft.news
msft.splits
msft.dividends
msft.actions



# get historical market data
hist = msft.history(period="1mo")
msft.history_metadata