import tkinter as tk

root = tk.Tk()
root.title("Mandelbrot Explorer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()
canvas.create_rectangle(50, 50, 100, 100, fill="red")
canvas.create_oval(150, 50, 200, 100, fill="blue")
canvas.create_text(300, 75, text="Hello!")

root.mainloop()