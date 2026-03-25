import tkinter as tk

window = tk.Tk()
window.title("GANAC_HO_EXAM")
window.geometry("650x200")
window.configure(bg="white")
window.resizable(False,False)



def register_win():
        if reg_btn:
            Window2 = tk.Toplevel(window)
            Window2.title("GANAC_HO_Exam")
            Window2.geometry("450x300")
            Window2.configure(bg = "green")
            Window2 = tk.Label(Window2, text = "You Have Succesfully Registered!", font = ("Arial", 10),bg = "green").grid(row=0,column=2,padx=5,pady=5)
            Username = tk.Label(Window2, text = "Username", font = ("Arial", 10), fg = "black").grid(row=1, column = 1,pady=5,padx=5)


def login_win():
      if log_btn:
            Window3 = tk.Toplevel(window)
            Window3.title("GANAC_HO_Exam")
            Window3.geometry("450x300")
            Window3.configure(bg = "red")
            Window3 = tk.Label(Window3, text = "Log in", font = ("Arial", 10, "bold")).grid(row=0,column=1, padx=5,pady=5)


title = tk.Label(window, text = "Welcome!", font = ("Arial", 20, "bold"))
title.pack(pady=5)
reg_btn = tk.Button(window, text = "register", font = ("Arial", 20, "bold"), command = register_win, bg = "blue")
reg_btn.pack(fill= 'x')
log_btn = tk.Button(window, text = "Log in", font = ("Arial", 20, "bold"), command = login_win,bg = "green" )
log_btn.pack(fill='x')








window.mainloop()