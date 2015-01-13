#!/usr/bin/env python3

"""
A simple GUI for reading .csv-files and perform statistical operations
on selected columns of the file
"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import statistics
import read_csv

def open_file(*args):
    """
    Opens a .csv-File and returns headers in a list
    """
    
    tmp_filename = filedialog.askopenfilename()
    filename.set(tmp_filename)
    tmp_header = read_csv.read_csv(tmp_filename)
    tmp_header_new = checkheader(tmp_header)
    header.set("")
    result.set("")
    column = ttk.Combobox(mainframe, textvariable=header, values=tmp_header_new).grid(column=2, row=2, sticky=(W, E))
    # enable or disable options if header is empty
    if tmp_header_new:
        create_options(True)
    else:
        create_options(False)

def checkheader(header_values):
    """
    Checks if headers can be calculated with all create_options
    if not, header is removed from list
    """
    
    for i, key in enumerate(header_values):
        try:
            statistics.calc_mean(filename.get(), key)
            statistics.calc_stddev(filename.get(), key)
            statistics.calc_sum(filename.get(), key)
            statistics.calc_variance(filename.get(), key)
            statistics.count(filename.get())
            statistics.find_max(filename.get(), key)
            statistics.find_min(filename.get(), key)
        except:
            header_values.pop(i)
    return header_values

def calculate(*args):
    """
    Main calculating function for statistical operations
    """
    
    key = header.get()
    
    if key:
        if operation_choice.get() == "mean":
            result.set(statistics.calc_mean(filename.get(), key))
        elif operation_choice.get() == "stddev":
            result.set(statistics.calc_stddev(filename.get(), key))
        elif operation_choice.get() == "sum":
            result.set(statistics.calc_sum(filename.get(), key))
        elif operation_choice.get() == "variance":
            result.set(statistics.calc_variance(filename.get(), key))
        elif operation_choice.get() == "count":
            result.set(statistics.count(filename.get()))
        elif operation_choice.get() == "max":
            result.set(statistics.find_max(filename.get(), key))
        elif operation_choice.get() == "min":
            result.set(statistics.find_min(filename.get(), key))

def create_options(enabled):
    """
    Creates options to choose statistical operation and either enable or disable them
    """
    
    if enabled == True:
        state="enabled"
    else:
        state="disabled"
    operation_choice.set("")
    root.calc_mean = ttk.Radiobutton(checkboxframe, text="Mean", variable=operation_choice, value="mean", state=state)
    root.calc_mean.grid(column=1, row=1, sticky=W)
    root.calc_stddev = ttk.Radiobutton(checkboxframe, text="Standard Deviation", variable=operation_choice, value="stddev", state=state)
    root.calc_stddev.grid(column=1, row=2, sticky=W)
    root.calc_sum = ttk.Radiobutton(checkboxframe, text="Sum", variable=operation_choice, value="sum", state=state)
    root.calc_sum.grid(column=1, row=3, sticky=W)
    root.calc_variance = ttk.Radiobutton(checkboxframe, text="Variance", variable=operation_choice, value="variance", state=state)
    root.calc_variance.grid(column=1, row=4, sticky=W)
    root.count = ttk.Radiobutton(checkboxframe, text="Count items", variable=operation_choice, value="count", state=state)
    root.count.grid(column=2, row=1, sticky=W)
    root.find_max = ttk.Radiobutton(checkboxframe, text="Find maximum", variable=operation_choice, value="max", state=state)
    root.find_max.grid(column=2, row=2, sticky=W)
    root.find_min = ttk.Radiobutton(checkboxframe, text="Find minimum", variable=operation_choice, value="min", state=state)
    root.find_min.grid(column=2, row=3, sticky=W)

def exit_program(*args):
    """
    Terminates the program
    """
    
    root.quit()
    
root = Tk()
root.title("Statistics Tool")

# create mainframe and the frame for operations choice
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

checkboxframe = ttk.Frame(mainframe)
checkboxframe.grid(column=2, row=3, sticky=(N, W, E, S))

filename = StringVar()
operation_choice = StringVar()
result = StringVar()
header = StringVar()

# Labels
ttk.Label(mainframe, text="Select File").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Select Column").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Select Operation").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Result").grid(column=1, row=4, sticky=W)

# Resultentry
ttk.Entry(mainframe, textvariable=result, state="disabled").grid(column=2, row=4, sticky=(W, E))

# File input field + button
file_entry = ttk.Entry(mainframe, textvariable=filename, state="disabled")
file_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Open", command=open_file).grid(column=3, row=1, sticky=W)

# Choose Column (just temporary, real combobox is initialized in open_file-function)
column = ttk.Combobox(mainframe, state="disabled").grid(column=2, row=2, sticky=(W, E))

# Choose operation
create_options(False)

# Calculation Button
calc_button = ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=(W, S))

# Exit Button
ttk.Button(mainframe, text="Exit", command=exit_program).grid(column=3, row=5, sticky=(W, S))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

file_entry.focus()
root.bind('<Return>', open_file)

root.mainloop()
