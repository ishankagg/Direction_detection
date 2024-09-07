import yfinance as yf

def get_data(ticker):
    data = yf.Ticker(ticker)
    data_df = data.history(period="max")
    print(f"Data for {ticker} downloaded")
    data_df.to_csv(f"data/{ticker}.csv")
    print(f"Data for {ticker} saved to data/{ticker}.csv") 
    return data_df

icici = "ICICIBANK.NS"
get_data(icici)