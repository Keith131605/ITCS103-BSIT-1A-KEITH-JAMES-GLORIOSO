import tkinter as tk

window = tk.Tk()

window.title("Student Profile")
window.geometry("500x500")
window.resizable(True,False)
window.configure(bg="purple",cursor="hand2")

label = tk.Label(window,text="Student Profile",font=("Poppins",40,"bold"),fg="Black",bg="purple",anchor="center")
label.pack(padx=30,pady=20)
tk.Label(window,text="NAME: Keith James Glorios\n\n\rAge: 19 years old\n\n\rCourse: BSIT-1A\n\n\rBirthday: December 13, 2006\n\n\rMotto:\n\n\rheelo",font=("Poppins",15,"bold"),fg="Black",bg="purple").pack(padx=3,pady=2,anchor="w")


window.mainloop()