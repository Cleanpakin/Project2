from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from Graph import currency_chart

# Color code
color1 = '#2e2c75'
color2 = '#11114f'
color3 = '#ffffff'
color4 = '#888dc9'
color5 = '#7efdd2'

def setting_UI(currency):
    # Create setting UI
    chart_option = Toplevel()
    chart_option.geometry('300x320')
    chart_option.title('Chart Setting')
    chart_option.resizable(height = False, width = False)

    # Add frame and background
    chart_main = Frame(chart_option, width = 300, height = 320, bg=color2)
    chart_main.grid(row=0, column=0)

    # Add title
    setting_icon = Image.open('image/Setting.png')
    setting_icon = setting_icon.resize((25,25))
    setting_icon = ImageTk.PhotoImage(setting_icon)

    setting_title = Label(
        chart_main,
        image=setting_icon,
        compound=RIGHT,
        text = 'Chart Setting',
        height=5,
        padx=9,
        pady=15,
        anchor=CENTER,
        font=('root 16 bold'),
        bg=color2,
        fg=color3
    )
    setting_title.place(x=60, y=7)

    # Add chart type button
    chart_text = Label(
        chart_main,
        text = 'Choose Chart Type',
        width=20,
        height=1,
        padx=0,
        pady=0,
        relief='flat',
        anchor='w',
        font=('root 12 bold'),
        bg=color2,
        fg=color3
    )
    chart_text.place(x=45, y=50)

    chart_type = [
        ('Line','line'),
        ('Candles','candle'),
        ('Bars','ohlc'),
        ('Area','area')
        ]
    
    chart = StringVar()
    chart.set('a')

    num = 75

    for text, type in chart_type:
        chart_button = Radiobutton(
            chart_main,
            text = text,
            variable=chart,
            value=type,
            anchor='w',
            width=10,
            font=('root 10 bold'),
            bg=color2,
            fg=color3,
            activebackground=color2,
            activeforeground=color3,
            cursor='cross',
            selectcolor='#0B0B45'
        )
        chart_button.place(x=40, y=num)
        num+=23
    
    # Add indicator text
    indicator_text = Label(
        chart_main,
        text = 'Indicator Setting',
        width=20,
        height=1,
        padx=0,
        pady=0,
        relief='flat',
        anchor='w',
        font=('root 12 bold'),
        bg=color2,
        fg=color3
    )
    indicator_text.place(x=45, y=175)

    on_icon = Image.open('image/Switch-on.png')
    on_icon = on_icon.resize((35,35))
    on_icon = ImageTk.PhotoImage(on_icon)

    off_icon = Image.open('image/Switch-off.png')
    off_icon = off_icon.resize((35,35))
    off_icon = ImageTk.PhotoImage(off_icon)

    # Add moving average button
    global ma_is_on
    ma_is_on = False

    def ma_switch():
        global ma_is_on

        if ma_is_on:
            ma_button.config(image=off_icon)
            ma_is_on = False
        else:
            ma_button.config(image=on_icon)
            ma_is_on = True
    
    ma_button = Button(
        chart_main,
        image=off_icon,
        bg=color2,
        activebackground=color2,
        bd=0,
        cursor='cross',
        command=ma_switch
    )
    ma_button.place(x=45, y=200)

    ma_text = Label(
        chart_main,
        text = 'Moving Average',
        width=15,
        height=1,
        padx=0,
        pady=13,
        relief='flat',
        anchor='w',
        font=('root 10 bold'),
        bg=color2,
        fg=color3
    )
    ma_text.place(x=88, y=195)

    ma_number = Entry(chart_main, width=8, justify=CENTER, font=('root 10'), relief=SOLID)
    ma_number.place(x=200, y=208)

    # Add volume button
    global v_is_on
    v_is_on = False

    def v_switch():
        global v_is_on

        if v_is_on:
            v_button.config(image=off_icon)
            v_is_on = False
        else:
            v_button.config(image=on_icon)
            v_is_on = True
    
    v_button = Button(
        chart_main,
        image=off_icon,
        bg=color2,
        activebackground=color2,
        bd=0,
        cursor='cross',
        command=v_switch
    )
    v_button.place(x=45, y=232)

    v_text = Label(
        chart_main,
        text = 'Volume',
        width=10,
        height=1,
        padx=0,
        pady=13,
        relief='flat',
        anchor='w',
        font=('root 10 bold'),
        bg=color2,
        fg=color3
    )
    v_text.place(x=88, y=227)

    # Add setting button
    def clicked_item():
        if chart.get() == 'a':
            messagebox.showinfo(message='Please select the chart type.')
        else:
            if ma_is_on and ma_number.get() == '':
                messagebox.showinfo(message='Please enter the moving average number.')
            else:
                item = chart.get()
                number = ma_number.get()
                chart_option.destroy()
                currency_chart(
                    item=item,
                    ma=ma_is_on,
                    v=v_is_on,
                    number=number,
                    currency=currency
                )

    finish = Button(
        chart_main,
        text='Create Chart',
        width=18,
        padx=5,
        height=1,
        bg=color1,
        fg=color3,
        activebackground=color1,
        activeforeground=color3,
        font=('root 12 bold'),
        cursor='cross',
        command=clicked_item
    )
    finish.place(x=50, y=270)

    chart_option.mainloop()
