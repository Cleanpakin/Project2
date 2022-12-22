from tkinter import Tk, ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

from Setting import *

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt

# Read csv file
crypto = []
df = pd.read_csv('Cryptocurrency Dataset.csv')
for i in df['Name']:
    crypto.append(i)

# Color code
color1 = '#2e2c75'
color2 = '#11114f'
color3 = '#ffffff'
color4 = '#888dc9'
color5 = '#7efdd2'

# Create main UI
window = Tk()
window.geometry('300x320')
window.title('Converter')
window.resizable(height = False, width = False)

# Add frame and background
top = Frame(window, width = 300, height = 60, bg=color2)
top.grid(row=0, column=0)

main = Frame(window, width = 300, height = 260, bg=color2)
main.grid(row=1, column=0)

# Add name and icon
icon = Image.open('image/Coin.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)

# Add title
app_name = Label(
    top,
    image = icon,
    compound=LEFT,
    text = 'Crypto to USD Converter',
    height=5,
    padx=9,
    pady=35,
    anchor=CENTER,
    font=('root 14 bold'),
    bg=color2,
    fg=color3
)
app_name.place(x=0, y=0)

# Add result box
result = Label(
    main,
    text = '',
    width=19,
    height=1,
    pady=3,
    anchor=CENTER,
    font=('root 13 bold'),
    bg=color1,
    fg=color3
)
result.place(x=50, y=15)

# Add search text and box
search_text = Label(
    main,
    text = 'Search Here',
    width=10,
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=CENTER,
    font=('root 12 bold'),
    bg=color2,
    fg=color3
)
search_text.place(x=96, y=60)

def search(event):
    value = event.widget.get()
    if value == '':
        combo_box['values'] = crypto
    else:
        coin_search = []

        for item in crypto:
            if value.lower() in item.lower():
                coin_search.append(item)
        combo_box['values'] = coin_search

combo_box = ttk.Combobox(
    main,
    value=crypto,
    width=25,
    justify=LEFT,
    font=('root 10')
)
combo_box.place(x=50, y=90)
combo_box.bind('<KeyRelease>',search)

# Add number text and box
number_text = Label(
    main,
    text = 'Number Here',
    width=20,
    height=1,
    padx=0,
    pady=0,
    relief='flat',
    anchor=W,
    font=('root 12 bold'),
    bg=color2,
    fg=color3
)
number_text.place(x=47, y=120)

number = Entry(main, width=10, justify=CENTER, font=('root 12'), relief=SOLID)
number.place(x=154, y=120)

# Convert function
def convertion():
    if combo_box.get() == '':
        messagebox.showinfo(message='Please select the currency.')
    elif number.get() == '':
        messagebox.showinfo(message='Please enter the number.')
    elif float(number.get()) <= 0:
        messagebox.showinfo(message='The number must be more than 0.')
    else:
        currency = combo_box.get()
        amount = float(number.get())
        n = 0
        for i in crypto:
            if i == currency:
                symbol = df['Symbol'][n]
            else:
                n+=1
        
        yf.pdr_override()
        realtime = dt.datetime.now()
        realtimedata = pdr.get_data_yahoo(f'{symbol}-USD',end = realtime)
        exchange = float(realtimedata['Close'][-1])
        converted = exchange*amount
        if converted > 0.01:
            result['text'] = '%.2f$'%converted
        else:
            result['text'] = '%f$'%converted

# Button's color change
def on_enter(e):
    e.widget.config(bg=color5)

def on_leave(e):
    e.widget.config(bg=color1)

# Add convert button
convert = Button(
    main,
    text='Convert',
    width=18,
    padx=5,
    height=1,
    bg=color1,
    fg=color3,
    activebackground=color1,
    activeforeground=color3,
    font=('root 12 bold'),
    cursor='exchange',
    command=convertion
)
convert.bind("<Enter>", on_enter)
convert.bind("<Leave>", on_leave)
convert.place(x=50, y=160)

# Graph setting window
def graph_window():
    if combo_box.get() == '':
        messagebox.showinfo(message='Please select the currency.')
    else:
        currency = combo_box.get()
        setting_UI(currency=currency)

# Add currency chart button
history = Button(
    main,
    text='Cryptocurrency Chart',
    width=18,
    padx=5,
    height=1,
    bg=color1,
    fg=color3,
    activebackground=color1,
    activeforeground=color3,
    font=('root 12 bold'),
    cursor='cross',
    command=graph_window
)
history.bind("<Enter>", on_enter)
history.bind("<Leave>", on_leave)
history.place(x=50, y=200)

window.mainloop()
