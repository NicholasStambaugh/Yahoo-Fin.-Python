import yfinance as yf
import pandas as pd

etfs = ['voo', 'ms', 'inds', 'xlsr', 'iyr', 'spy', 'qqq', 'msft', 'vt', 'sdy', 'cqqq', 'soxl', 'spem', 'googl', 'wmt', 'ivv', 'vxus', 'agg', 'schd']

df = pd.DataFrame()

today = datetime.now().date().strftime("%Y-%m-%d")

for etf in etfs:
    df[etf] = yf.Ticker(etf).history(start="2010-09-08", end=today).Close

df = df.diff()
print(df.diff())

df = df.corr()
print(df.corr())
