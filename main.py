import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk  # new


def convert():
    try:
        mile = entry_int.get()
    except Exception as e:
        entry_int.set(0)
        mile = entry_int.get()

    km = mile * 1.61
    output_str.set(f'{km:,.2f} km')


# window
# window = tk.Tk()  # ddefault

# window
window = ttk.Window(themename='journal')  # bootstrap new
# window title
window.title('Demo M2K')
# (width x height)
window.geometry('350x150')

# body title
title_lb = ttk.Label(master=window, text='Miles 2 Kilometres', font='Calibri 24 bold')
title_lb.pack(pady=10)

# input filed
input_f = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry_num = ttk.Entry(master=input_f, textvariable=entry_int, justify='left')

# button
convert_btn = ttk.Button(master=input_f, text='Convert', command=convert)
entry_num.pack(side='left', padx=10)
convert_btn.pack(side='left')
input_f.pack(pady=10)

# output
output_str = tk.StringVar()
output_lb = ttk.Label(master=window, text='Output', font='Calibri 20', textvariable=output_str)
output_lb.pack()

# run
window.mainloop()
