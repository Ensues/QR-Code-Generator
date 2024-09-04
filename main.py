# Importing Modules

import qrcode, PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Logic 

def createQR(*args):
    data = text_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black").convert('RGB')  # Customize colors
        res_img = img.resize((280, 250), Image.LANCZOS)  # Resize QR code image
        tkimage = ImageTk.PhotoImage(res_img)
        qr_canvas.delete('all')
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        try:
            img = Image.open("dissapointment.png")
            img_resized = img.resize((280, 250), Image.LANCZOS)  # Resize image to fit canvas
            tkimage = ImageTk.PhotoImage(img_resized)
            qr_canvas.delete('all')
            qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
            qr_canvas.image = tkimage
            messagebox.showwarning("Warning", 'Enter Data in Entry First')
        except FileNotFoundError:
            messagebox.showwarning("Warning", 'Enter Data in Entry First')


def saveQR(*args):
    data = text_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black").convert('RGB')  # Customize colors
        res_img = img.resize((280, 250), Image.LANCZOS)  # Resize QR code image
        
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            res_img.save(path)
            messagebox.showinfo("Success", "QR Code is Saved")
    else:
        try:
            img = Image.open("dissapointment.png")
            img_resized = img.resize((280, 250), Image.LANCZOS)  # Resize image to fit canvas
            tkimage = ImageTk.PhotoImage(img_resized)
            qr_canvas.delete('all')
            qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
            qr_canvas.image = tkimage
            messagebox.showwarning("Warning", 'Enter Data in Entry First')
        except FileNotFoundError:
            messagebox.showwarning("Warning", 'Enter Data in Entry First')

# GUI Code

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x380")
root.config(bg='black')
root.resizable(0,0)

frame1 = tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=10,y=5,width=280,height=250)

frame2 = tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=10,y=260,width=280,height=100)

try:
    cover_img = Image.open("qrCodeCover.png")
    cover_img_resized = cover_img.resize((280, 250), Image.LANCZOS)  # Resize cover image to fit canvas
    cover_img_tk = ImageTk.PhotoImage(cover_img_resized)
    qr_canvas = tk.Canvas(frame1)
    qr_canvas.bind("<Double-1>", saveQR)
    qr_canvas.create_image(0, 0, anchor=tk.NW, image=cover_img_tk)
    qr_canvas.image = cover_img_tk
except FileNotFoundError:
    qr_canvas = tk.Canvas(frame1)
    qr_canvas.bind("<Double-1>", saveQR)
    qr_canvas.create_text(140, 125, text="No Cover Image", font=("Arial", 20), fill="white")

qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=5)

btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x=25, y=50)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x=100, y=50)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x=175, y=50)

root.mainloop()