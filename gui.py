# Part 2 (STRETCH) - a small graphical interface (GUI) with tkinter: a tip calculator.
#
# The window and its widgets are built for you. Write the `calculate` function so that,
# when the button is clicked, it reads the bill amount, works out a 15% tip and the
# total, and shows them in the result label.
#
# There is no automated test for this part (a GUI can't be checked that way) - show it
# to your lab instructor.

import tkinter as tk


def calculate():
    #bill = float(entry.get() or 0)#Either inputs the entry when available, or will put 0 whenever entry is empty; This will break if the input is non numeric;
    bill = float(entry.get()) if entry.get().replace(".", "").isdecimal() else 0#will only recive floats and will not break with non numeric inputs; This could also be done as something similar or even better using a proper if statements;
    tip = bill * 0.15
    total = bill + tip

    result.config(text=f"Tip: ${tip:.2f}   Total: ${total:.2f}")


root = tk.Tk()
root.title("Tip Calculator")

tk.Label(root, text="Bill amount:").pack(padx=10, pady=(10, 0))
entry = tk.Entry(root)
entry.pack(padx=10, pady=4)
entry.focus_set() #Makes the code to work like google, so when I run the code, if I type anything, it will automaticly be inputed to the lable;

tk.Button(root, text="Calculate 15% tip", command=calculate).pack(padx=10, pady=4)
root.bind('<Return>', lambda event: calculate())
#root.bind('<KeyPress-Shift_L>', lambda event: calculate())

#root.bind() lets me to use a button to give me the output instead of just cliking on the button;

result = tk.Label(root, text="Tip: $0.00   Total: $0.00", font=("Arial", 12))
result.pack(padx=10, pady=10)

root.mainloop()