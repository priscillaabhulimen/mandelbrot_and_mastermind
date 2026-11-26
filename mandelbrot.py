import tkinter as tk

WIDTH, HEIGHT, MAX_ITER = 600, 550, 1000
CENTER_X, CENTER_Y = 0.0, 0.0
ZOOM = 1.0

render_generation = 0

# Create tk frame
root = tk.Tk()
root.geometry("600x600")
root.title("Mandelbrot visualisation")

# Create tk canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
image = tk.PhotoImage(width=WIDTH, height=HEIGHT)

# Convert pixel into complex number
def pixel_to_complex(x, y):
    # Real part
    real = CENTER_X + (x / WIDTH - 0.5) * 4 / ZOOM

    # Imaginary part
    imaginary = CENTER_Y - (0.5 - y/HEIGHT) * 4 / ZOOM

    return complex(real,imaginary)

# How long before the value becomes unbounded
def escape_time(c):
    n = 0
    z = 0
    while n < MAX_ITER and abs(z) <= 2:
        z = z**2 + c
        n += 1

    return n

def pixel_colours(start_row=0, generation=None):
    global render_generation

    if generation is None:
        render_generation += 1
        generation = render_generation

    if generation != render_generation:
        return

    for row in range(start_row, min(start_row + 5, HEIGHT)):
        row_colours = []

        for col in range(WIDTH):
            n = escape_time(pixel_to_complex(col, row))
            row_colours.append(choose_colour(n))

        image.put("{" + " ".join(row_colours) + "}", to=(0, row))

    if start_row + 5 < HEIGHT:
        root.after(1, pixel_colours, start_row + 5, generation)

def choose_colour(n):
    if n == MAX_ITER:
        return "#000000"

    if n < 90:
        start = (0, 0, 255)       # Blue
        end = (128, 0, 128)       # Purple
        t = n / 90

    elif n < 360:
        start = (128, 0, 128)     # Purple
        end = (173, 223, 255)     # Pale blue
        t = (n - 90) / 270

    else:
        start = (173, 223, 255)   # Pale blue
        end = (173, 223, 255)
        t = 1

    r = int(start[0] + (end[0] - start[0]) * t)
    g = int(start[1] + (end[1] - start[1]) * t)
    b = int(start[2] + (end[2] - start[2]) * t)

    return f"#{r:02X}{g:02X}{b:02X}"

def zoom_in():
    global ZOOM
    ZOOM *= 1.4
    pixel_colours()

def zoom_out():
    global ZOOM
    ZOOM /= 1.4
    pixel_colours()

canvas.create_image((0, 0), image=image, anchor="nw")
canvas.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

zoom_in_button = tk.Button(
    button_frame,
    text="Zoom In",
    command=zoom_in
)
zoom_in_button.pack(side=tk.LEFT, padx=30)

zoom_out_button = tk.Button(
    button_frame,
    text="Zoom Out",
    command=zoom_out
)
zoom_out_button.pack(side=tk.LEFT, padx=30)

pixel_colours()
# start tk main loop
root.mainloop()