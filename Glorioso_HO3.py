import tkinter as tk

def add():
	num1 = label_entry.get()
	num2 = label2_entry.get()
	result = int(num1) + int(num2)
	outcome["text"] = f"The sum of {num1} + {num2} is {result}"
def substract():
	num1 = label_entry.get()
	num2 = label2_entry.get()
	result = int(num1) - int(num2)
	outcome["text"] = f"The difference of {num1} - {num2} is {result}"
def multiply():
	num1 = label_entry.get()
	num2 = label2_entry.get()
	result = int(num1) * int(num2)
	outcome["text"] = f"The product of {num1} x {num2} is {result}"
def divided():
	num1 = label_entry.get()
	num2 = label2_entry.get()
	if int(num2) != 0:
		result = int(num1) / int(num2)
		outcome["text"] = f"The quotient of {num1} / {num2} is {result}"
	else:
		outcome["text"] = f"Cannot Divide by 0"


window = tk.Tk()
window.title("Calculator Simulation")
window.resizable(False,False)
window.configure(bg="blue",cursor="hand1")

outcome = tk.Label(window, text = "Calculator Simulation")
outcome.grid(row = 0, column = 0)

frame=tk.Frame (window, bg="Lightblue")
frame.grid(padx=10)

name_label=tk. Label (frame, text="1st entry number", bg="orange", fg="black")
name_label.grid(row=2, column=0)
label_entry = tk. Entry (frame)
label_entry.grid(row=2, column=1, columnspan=1)
name_label2=tk.Label(frame, text="2nd entry number", bg="orange", fg="black")
name_label2.grid(column=0,row=3)
label2_entry= tk. Entry(frame)
label2_entry.grid(row=3, column=1, columnspan=2)

button=tk.Button(frame, text="ADDITION",command = add,font=("arial",10,"bold"),bg="yellow")
button.grid(row=6,column=0)
button=tk.Button(frame, text="MULTIPLICATION",command = multiply,font=("arial", 10,"bold"),bg="yellow")
button.grid(row=7,column=0)
button = tk.Button(frame,text="SUBTRACTION",command = substract,font=("arial", 10, "bold"),bg="yellow")
button.grid(row=6,column=1)
button = tk.Button(frame, text="DIVISION",command = divided,font=("arial",10,"bold"),bg="yellow")
button.grid(row=7,column=1)

window.mainloop()
