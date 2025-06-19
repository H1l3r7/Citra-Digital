import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
from image_processing import *

display_image = None
canvas = None
img_container = None
current_image_np = None

def show_on_canvas(image_cv):
    global display_image, current_image_np
    if image_cv is None:
        return
    current_image_np = image_cv.copy()
    if len(image_cv.shape) == 2:
        image_pil = Image.fromarray(image_cv).convert("L")
    else:
        image_rgb = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)
    image_pil = image_pil.resize((300, 300))
    display_image = ImageTk.PhotoImage(image_pil)
    canvas.itemconfig(img_container, image=display_image)

def open_image():
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if not path:
        return
    img = load_image(path)
    show_on_canvas(img)

def save_image():
    if current_image_np is None:
        print("⚠️ Tidak ada gambar yang bisa disimpan.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if save_path:
        if len(current_image_np.shape) == 2:
            img_to_save = current_image_np
        else:
            img_to_save = cv2.cvtColor(current_image_np, cv2.COLOR_RGB2BGR)
        cv2.imwrite(save_path, img_to_save)
        print(f"✅ Gambar berhasil disimpan: {save_path}")

def show_histogram():
    gray = get_gray_histogram()
    if gray is not None:
        plt.figure("Histogram Grayscale")
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.title("Histogram Grayscale")
        plt.xlabel("Intensitas")
        plt.ylabel("Jumlah Piksel")
        plt.grid()
        plt.show()

def create_gui():
    global canvas, img_container
    root = Tk()
    root.title("Pengolahan Citra Digital Interaktif")
    root.geometry("520x750")
    root.resizable(False, False)

    Label(root, text="📸 Pengolahan Citra Digital", font=("Arial", 16, "bold")).pack(pady=10)
    canvas = Canvas(root, width=300, height=300, bg="gray")
    canvas.pack()
    img_container = canvas.create_image(0, 0, anchor=NW)

    Button(root, text="📂 Pilih Gambar", width=35, command=open_image).pack(pady=5)
    Button(root, text="🖼️ Gambar Asli", width=35, command=lambda: show_on_canvas(get_original())).pack(pady=5)
    Button(root, text="⚫ Binary", width=35, command=lambda: show_on_canvas(get_binary())).pack(pady=5)
    Button(root, text="🚫 Operasi NOT", width=35, command=lambda: show_on_canvas(get_not())).pack(pady=5)
    Button(root, text="✨ Sharpen", width=35, command=lambda: show_on_canvas(get_sharpen())).pack(pady=5)
    Button(root, text="🎨 Grayscale", width=35, command=lambda: show_on_canvas(get_grayscale())).pack(pady=5)
    Button(root, text="💡 Tambah Terang", width=35, command=lambda: show_on_canvas(get_brightness())).pack(pady=5)
    Button(root, text="📊 Histogram", width=35, command=show_histogram).pack(pady=5)
    Button(root, text="🧽 Morfologi (Erosi)", width=35, command=lambda: show_on_canvas(get_erosi())).pack(pady=5)
    Button(root, text="💾 Simpan Gambar", width=35, command=save_image).pack(pady=5)

    Label(root, text="© 2025 | GUI by Tkinter & OpenCV", font=("Arial", 9)).pack(side="bottom", pady=10)
    root.mainloop()
