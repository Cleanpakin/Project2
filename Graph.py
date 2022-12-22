import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import mplfinance as mpf
import datetime as dt

# Read csv file
crypto = []
df = pd.read_csv('Cryptocurrency Dataset.csv')
for i in df['Name']:
    crypto.append(i)

# Set up chart
colors = mpf.make_marketcolors(
        up='#00ff00', 
        down='#ff0000', 
        wick='in', 
        edge='in',
        ohlc='in',
        volume='in'
    )

mpf_style = mpf.make_mpf_style(
        base_mpf_style='nightclouds',
        marketcolors=colors
    )

# Make chart
def currency_chart(item,ma,v,number,currency):
    start = dt.datetime(2019,1,1)
    end = dt.datetime.now()

    n = 0
    for i in crypto:
        if i == currency:
            symbol = df['Symbol'][n]
        else:
            n+=1

    yf.pdr_override()
    data = pdr.get_data_yahoo(f'{symbol}-USD',start,end)

    ma_list=[]
    text=''
    innumber = [x for x in number]
    for i in range(len(innumber)):
        if innumber[i] in '0123456789':
            text = text + number[i]
        if innumber[i] not in '0123456789' and text != '':
            ma_list.append(int(text))
            text = ''
        if i == len(number)-1 and number[i] in '0123456789':
            ma_list.append(int(text))
    
    if ma:
        if item == 'line':
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = item,
                style = mpf_style,
                linecolor = '#2a60f4',
                volume = v,
                mav = ma_list
            )

        elif item == 'candle' or item == 'ohlc':
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = item,
                style = mpf_style,
                volume = v,
                mav = ma_list
            )

        else:
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = 'line',
                style = mpf_style,
                linecolor = '#2a60f4',
                fill_between = dict(y1=data['Close'].values,color = '#141c34'),
                volume = v,
                mav = ma_list
            )
    else:
        if item == 'line':
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = item,
                style = mpf_style,
                linecolor = '#2a60f4',
                volume = v
            )

        elif item == 'candle' or item == 'ohlc':
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = item,
                style = mpf_style,
                volume = v
            )

        else:
            mpf.plot(
                data,
                axtitle = f'{currency} Chart',
                xlabel = 'Date',
                ylabel = 'Price (USD)',
                type = 'line',
                style = mpf_style,
                linecolor = '#2a60f4',
                fill_between = dict(y1=data['Close'].values,color = '#141c34'),
                volume = v
            )
