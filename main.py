import tkinter as tk
from tkinter import filedialog, messagebox, IntVar, Radiobutton
from PIL import Image

def resize_and_compress(image_path, output_path, resize_percentage, desired_width, desired_height, quality, format, resize_choice):
    try:
        quality = int(quality)  # Convert quality to integer
        with Image.open(image_path) as img:  # Open image to be resized
            # Resize according to percentage or specific dimensions
            if resize_choice == 1:  # Resize by percentage
                resize_percentage = float(resize_percentage) / 100
                new_width = int(img.width * resize_percentage)
                new_height = int(img.height * resize_percentage)
            else:  # Resize by custom dimensions
                new_width = int(desired_width)
                new_height = int(desired_height)

            img_resized = img.resize((new_width, new_height), Image.LANCZOS)  # Resize image with LANCZOS filter (high-quality)
            # Save image in specific format (JPEG or PNG)
            if format == 'PNG':
                img_resized.save(output_path, format='PNG')
            else:
                img_resized.save(output_path, format='JPEG', quality=quality)
            return f"Image resized, saved to {output_path}, Size: {new_width}x{new_height}, Quality: {quality if format == 'JPEG' else 'Lossless'}, Format: {format}"
    except Exception as e:  # Return error, if any
        return str(e)

def open_file_dialog(entry_widget):
    # Open file dialog to select an image and insert its path to entry widget
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def save_file_dialog(entry_widget):
    # Open file dialog to select output path and insert it to entry widget
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("WebP", "*.webp")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def perform_resize():
    # Collect inputs from UI and call resize_and
    image_path = entry_input.get()
    output_path = entry_output.get()
    resize_percentage = entry_percentage.get()
    desired_width = entry_width.get()
    desired_height = entry_height.get()
    quality = entry_quality.get()
    format = 'PNG' if output_path.lower().endswith('.png') else 'JPEG'
    resize_choice = resize_option.get()
    message = resize_and_compress(image_path, output_path, resize_percentage, desired_width, desired_height, quality, format, resize_choice)
    messagebox.showinfo("Result", message)

app = tk.Tk()
app.title("Image Resizer and Compressor")

resize_option = IntVar(value=1)  # Default to resize by percentage

tk.Label(app, text="Input Path:").grid(row=0, column=0)
entry_input = tk.Entry(app, width=50)
entry_input.grid(row=0, column=1)
button_input = tk.Button(app, text="Browse", command=lambda: open_file_dialog(entry_input))
button_input.grid(row=0, column=2)

tk.Label(app, text="Output Path:").grid(row=1, column=0)
entry_output = tk.Entry(app, width=50)
entry_output.grid(row=1, column=1)
button_output = tk.Button(app, text="Browse", command=lambda: save_file_dialog(entry_output))
button_output.grid(row=1, column=2)

Radiobutton(app, text="Resize by Percentage", variable=resize_option, value=1).grid(row=2, column=0)
entry_percentage = tk.Entry(app, width=50)
entry_percentage.grid(row=2, column=1)

Radiobutton(app, text="Resize by Width & Height", variable=resize_option, value=2).grid(row=3, column=0)
tk.Label(app, text="Width:").grid(row=4, column=0)
entry_width = tk.Entry(app, width=50)
entry_width.grid(row=4, column=1)
tk.Label(app, text="Height:").grid(row=5, column=0)
entry_height = tk.Entry(app, width=50)
entry_height.grid(row=5, column=1)

tk.Label(app, text="Quality (1-100):").grid(row=6, column=0)
entry_quality = tk.Entry(app, width=50)
entry_quality.grid(row=6, column=1)

button_compress = tk.Button(app, text="Resize and Compress", command=perform_resize)
button_compress.grid(row=7, column=1)

app.mainloop()
