#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=200, width=200)
        frame2 = ttk.Frame(toplevel1)
        frame2.configure(height=200, width=200)
        treeview1 = ttk.Treeview(frame2)
        treeview1.configure(selectmode="none")
        treeview1.grid(column=0, row=0)
        entry1 = ttk.Entry(frame2)
        entry1.grid(column=1, row=0)
        button1 = ttk.Button(frame2)
        button1.configure(
            compound="top",
            cursor="arrow",
            takefocus=False,
            text='button1')
        button1.place(anchor="nw", relx=0.71, rely=0.58, x=0, y=0)
        frame2.grid(column=0, row=0)
        frame2.rowconfigure(0, pad=10)
        frame2.columnconfigure(0, pad=10)

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = NewprojectApp()
    app.run()

