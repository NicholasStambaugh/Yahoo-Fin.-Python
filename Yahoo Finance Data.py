import pandas as pd
import yfinance as yf
from datetime import datetime
plt.style.use('seaborn')
msft = yf.Ticker("MSFT")

#since its a dictionary, we need to store it in a variable
stockinfo = msft.info

#dictonary loop, prints line by line
for key,value in stockinfo.items():
    print(key, ":", value)

#return one value from info
numshares = msft.info['sharesOutstanding']
print(numshares)

# get stock info
msft.info
# get historical market data
msft.history(period="max")
# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

#show current analyst reccomednations
msft.recommendations

#see major holders
msft.major_holders

#go more in depth, view the institutions holding microsoft stock
msft.institutional_holders

#we know from earlier we can just store this in a variable, using print to see column names
df = msft.institutional_holders
print(df)

#analyze institutional holders using matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(10,8), dpi=62) #adjust figure size, fonts will adjust
plt.bar(df['Holder'],df['% Out'])
plt.ylabel('% Holder of Microsoft')
plt.xlabel('Holder')
plt.title('Microsoft Major Holders')
plt.show()


#lets go into the dividends
div = msft.dividends

#changing the date column
#start off by getting a sum of dividends per year
data = div.resample('Y').sum()

#reset index allows us to create a new colum called year
data = data.reset_index()
data['Year'] = data['Date'].dt.year #new column

#analyze dividends overtime
plt.figure()
plt.bar(data['Year'],data['Dividends'])
plt.ylabel('Dividend Yield in $')
plt.xlabel('Year')
plt.title('Microsoft Dividend History')
plt.xlim(2002,2023) #adjust limits
plt.style.use('seaborn')

#balance sheet
print(msft.balancesheet)

#financials
print(msft.financials)

#cashflow
print(msft.cashflow)

#exploring price
hist = msft.history(period="1mo") #adjust date here, can also do start & end dates
plt.figure()
plt.plot(hist['Close']) #basic price plot, open, close, high
plt.show()

#etfs
security = yf.Ticker("VOO")

#exploring price
hist1 = security.history(period="max") #adjust date here, can also do start & end dates
plt.figure()
plt.plot(hist1['Close'])#basic price plot, open, close, high
plt.ylabel('Price')
plt.xlabel('Year')
plt.show()

#dowjones industrial average
djia = yf.Ticker("djia")

#price
hist2 = djia.history(period="max") #adjust date here, can also do start & end dates
plt.figure()
plt.plot(hist2['Close'])#basic price plot, open, close, high
plt.ylabel('Price')
plt.xlabel('Year')
plt.show()


#price of stock or market historical basis to today

#creating today variable
today = datetime.now().date().strftime("%Y-%m-%d")

#spy
spy = yf.Ticker("SPY")

#exploring price
hist4 = spy.history(start="2007-01-01", end=today) #adjust date here, can also do start & end dates
plt.figure()
plt.plot(hist2['Close'])#basic price plot, open, close, high
plt.ylabel('Price')
plt.xlabel('Year')
plt.show()


#combine index to stocks
securities = ['voo', 'msft', 'crm', 'axp', 'aapl', 'tsla', 'nvda']

dfs = pd.DataFrame()

for securityy in securities:
    dfs[securityy] = yf.Ticker(securityy).history(start="2007-01-01", end=today).Close


#need to add legend...sorry
plt.figure()
plt.plot(dfs)#basic price plot, open, close, high
plt.ylabel('Price')
plt.xlabel('Year')
plt.show()
