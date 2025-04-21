import tkinter as tk
from tkinter import filedialog, Scrollbar, Canvas
from PIL import Image, ImageTk
import pytesseract

# Uncomment and set the path if needed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
    if file_path:
        # Load image
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        # Display image on canvas
        canvas.image = photo
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo)
        canvas.config(scrollregion=canvas.bbox("all"))

        # Extract text
        extracted = extract_text_from_image(image)
        text_label.config(text=extracted.strip() or "[No text found]")

# Set up main window
root = tk.Tk()
root.title("Image OCR Viewer")
root.geometry("900x700")

# Browse button
browse_btn = tk.Button(root, text="Browse Image", command=open_image)
browse_btn.pack(pady=5)

# Scrollable canvas for image display
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

canvas = Canvas(frame, bg="grey")
canvas.pack(side="left", fill="both", expand=True)

scroll_y = Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_y.pack(side="right", fill="y")
canvas.config(yscrollcommand=scroll_y.set)

scroll_x = Scrollbar(root, orient="horizontal", command=canvas.xview)
scroll_x.pack(fill="x")
canvas.config(xscrollcommand=scroll_x.set)

# Label for extracted text
text_label = tk.Label(root, text="", wraplength=850, justify="left", anchor="w", bg="#f0f0f0", font=("Arial", 10))
text_label.pack(fill="both", expand=False, padx=10, pady=10)

# Start app
root.mainloop()
