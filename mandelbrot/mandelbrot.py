
import tkinter as tk
import numpy as np

WIDTH, HEIGHT, MAX_ITER = 600, 550, 1000

CENTER_X, CENTER_Y = 0.0, 0.0
ZOOM = 1.0

render_generation = 0
click_timer = None

# Create Tkinter window
root = tk.Tk()
root.geometry("620x640")
root.title("Mandelbrot Visualisation")

# Create canvas and image
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
image = tk.PhotoImage(width=WIDTH, height=HEIGHT)

canvas.create_image(0, 0, image=image, anchor="nw")
canvas.pack()


# Convert pixel coordinates into complex coordinates
def pixel_to_complex(x, y):
    real = CENTER_X + (x / WIDTH - 0.5) * 4 / ZOOM
    imaginary = CENTER_Y + (0.5 - y / HEIGHT) * 4 / ZOOM

    return real + 1j * imaginary


# Calculate escape times for an entire row using NumPy
def calculate_escape_times(row):
    x = np.arange(WIDTH)
    real = CENTER_X + (x / WIDTH - 0.5) * 4 / ZOOM
    imaginary = CENTER_Y + (0.5 - row / HEIGHT) * 4 / ZOOM

    C = real + 1j * imaginary

    Z = np.zeros(WIDTH, dtype=complex)
    escape_times = np.zeros(WIDTH, dtype=int)

    active = np.ones(WIDTH, dtype=bool)

    for n in range(MAX_ITER):
        Z[active] = Z[active] ** 2 + C[active]

        escaped = np.abs(Z) > 2
        newly_escaped = active & escaped

        escape_times[newly_escaped] = n + 1
        active[newly_escaped] = False

        if not np.any(active):
            break

    escape_times[active] = MAX_ITER

    return escape_times


# Convert escape time into a colour
def choose_colour(n):
    if n == MAX_ITER:
        return "#000000"

    if n < 90:
        start = (0, 0, 255)
        end = (128, 0, 128)
        t = n / 90

    elif n < 360:
        start = (128, 0, 128)
        end = (173, 223, 255)
        t = (n - 90) / 270

    else:
        start = (173, 223, 255)
        end = (173, 223, 255)
        t = 1

    r = int(start[0] + (end[0] - start[0]) * t)
    g = int(start[1] + (end[1] - start[1]) * t)
    b = int(start[2] + (end[2] - start[2]) * t)

    return f"#{r:02X}{g:02X}{b:02X}"


# Render the image in batches
def pixel_colours(start_row=0, generation=None):
    global render_generation

    if generation is None:
        render_generation += 1
        generation = render_generation

    if generation != render_generation:
        return

    end_row = min(start_row + 5, HEIGHT)

    for row in range(start_row, end_row):
        escape_times = calculate_escape_times(row)

        row_colours = [
            choose_colour(n) for n in escape_times
        ]

        image.put(
            "{" + " ".join(row_colours) + "}",
            to=(0, row)
        )

    if end_row < HEIGHT:
        root.after(
            1,
            pixel_colours,
            end_row,
            generation
        )


def zoom_at(event):
    global CENTER_X, CENTER_Y, ZOOM

    # Ignore clicks outside the image
    if not (0 <= event.x < WIDTH and 0 <= event.y < HEIGHT):
        return

    # Find the complex coordinate under the mouse
    clicked_point = pixel_to_complex(event.x, event.y)

    # Make that point the new centre
    CENTER_X = clicked_point.real
    CENTER_Y = clicked_point.imag

    # Zoom in
    ZOOM *= 2

    # Redraw
    pixel_colours()

def single_click_zoom(event):
    global click_timer

    # Cancel any previously scheduled single-click
    if click_timer is not None:
        root.after_cancel(click_timer)

    # Wait briefly to see whether a second click occurs
    click_timer = root.after(
        250,
        lambda: zoom_at(event)
    )


def double_click_zoom(event):
    global click_timer, ZOOM

    # Cancel the pending single-click
    if click_timer is not None:
        root.after_cancel(click_timer)
        click_timer = None

    # Zoom out
    ZOOM /= 2
    pixel_colours()

canvas.bind("<Button-1>", single_click_zoom)
canvas.bind("<Double-Button-1>", double_click_zoom)

# Initial rendering
pixel_colours()

root.mainloop()
