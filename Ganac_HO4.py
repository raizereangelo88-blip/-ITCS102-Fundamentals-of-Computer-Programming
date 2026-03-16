import tkinter as tk


window = tk.Tk()
window.title("Profile Builder")
window.geometry("500x250")
window.config(bg="lightgreen")

tk.Label(window, text = "Profile Builder", font = ("Arial", 20), fg = "black", bg = "lightgreen").grid(row = 1, column = 0, padx = 50, pady = 30)
tk.Label(window, text = "First Name", font = ("Times New Roman", 10), fg ="black", bg = "lightgreen").grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 15)
tk.Label(window, text = "Middle Name", font = ("Times New Romanl", 10), fg ="black", bg = "lightgreen").grid(row = 2, column = 3, padx = 20, pady = 15)
tk. Label(window, text ="Last Name", font = ("Times New Roman", 10), fg ="black", bg="lightgreen").grid(row = 2, column = 4, padx = 20, pady = 15)
first_name= tk.StringVar()


frame1 = tk.Frame(window, bg = "lightgreen")
frame1.pack()


tk.Entry
tk.Button(window, text = "Submit").grid(row = 4, column = 0, padx  = 5, pady = 5)
window.mainloop()