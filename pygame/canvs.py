from tkinter import *

def keyEvent(event):
    if event.keysym == "Escape":
        tk.destroy()

tk = Tk()
# -------------------------------------
canvas = Canvas(tk, width=400, height=100, bg="#00ff00")
canvas.pack()
# -------------------------------------
tk.bind_all("<KeyPress>", keyEvent)
tk.lift()
tk.focus_force()
#tk.after(20000, tk.destroy)
tk.mainloop()
