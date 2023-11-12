import time
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk  # new


class TkWindow:
    def __init__(self):
        # self.window = tk.Tk()   # default
        self.window = ttk.Window(themename='litera')  # bootstrap - new
        self.geo = '300x150'
        self.title = 'Demo M2K'
        self.window.title(self.title)


class Mils2Kilometres(TkWindow):
    def __init__(self):
        super().__init__()
        self._entry_int = tk.IntVar()
        self._output_str = tk.StringVar()

    def __miles2km(self):
        try:
            miles = self._entry_int.get()
        except:
            self._entry_int.set(0)
            miles = 0

        # formula
        kilometres = miles * 1.61
        # print
        self._output_str.set(f'{kilometres:,.2f} km')

    def __index_tk(self):
        # label
        title_label = ttk.Label(master=self.window, text='Miles 2 Kilometres', font='Calibri 24 bold')
        title_label.pack(pady=10)

        # input field
        input_frame = ttk.Frame(master=self.window)
        entry_num = ttk.Entry(master=input_frame, textvariable=self._entry_int)
        # button
        convert_btn = ttk.Button(master=input_frame, text='Convert', command=self.__miles2km)
        entry_num.pack(side='left', padx=10)
        convert_btn.pack(side='left', padx=10)
        input_frame.pack(pady=10)

        # print
        print_label = ttk.Label(master=self.window, text='Output', font='Calibri 20', textvariable=self._output_str)
        print_label.pack(pady=10)

    def run(self):
        self.__index_tk()
        self.window.mainloop()


if __name__ == '__main__':
    km = Mils2Kilometres()
    km.run()
