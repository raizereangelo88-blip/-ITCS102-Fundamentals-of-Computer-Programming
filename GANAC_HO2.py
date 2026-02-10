
import tkinter as tk



window = tk.Tk()
window.title("My Profile")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg = "#191970")

StudentTitle = tk.Label(text = "Student Profile", font = ("Times New Roman", 20), bg="#191970")
StudentName = tk.Label(text = "Raizere Angelo Monton Gañac", font = ("Times New Roman", 20), bg="#191970")
StudentAge = tk.Label(text ="Age: 18", font = ("Times New Roman", 20), bg="#191970")
StudentAddress = tk.Label(text = "Barangay Kanlurang Mayao, Lucena City", font = ("Times New Roman", 20), bg="#191970")
StudentCourse = tk.Label(text = "Bachelor of Science in Information Technology", font = ("Times New Roman",20), bg="#191970")
StudentBirthday = tk.Label(text = "April 10, 2007", font = ("Times New Roman", 20), bg="#191970")
StudentQuote = tk.Label(text = "If it's meant to be, it will be", font = ("Times New Roman", 20), bg = "#191970")

StudentTitle.pack(pady=10)
StudentName.pack(pady=5)
StudentAge.pack(pady=5)
StudentAddress.pack(pady=5)
StudentCourse.pack(pady=5)
StudentBirthday.pack(pady=5)
StudentQuote.pack(pady=5)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
color_index = 0
fonts = [
    ("Times New Roman", 20),
    ("Arial", 20, "bold"),
    ("Courier New", 20, "italic"),
    ("Verdana", 20, "bold"),
    ("Impact", 20)
]

color_index = 0
font_index = 0

def animate_quote():
    global color_index, font_index

    StudentQuote.config(
    fg=colors[color_index], 
    font=fonts[font_index]) 
    color_index = (color_index + 1) % len(colors)
    font_index = (font_index + 1) % len(fonts)
    
    window.after(700, animate_quote) #

animate_quote()
def animate_text():
    global color_index
    StudentQuote.config(fg=colors[color_index])
    color_index = (color_index + 1) % len(colors)
    window.after(500, animate_text)


animate_text()
window.mainloop()