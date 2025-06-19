import cv2
import numpy as np
from matplotlib import pyplot as plt

# Variabel global
citra = None
citra_resized = None
gray = None
binary = None
last_image_shown = None  # Untuk menyimpan citra yang terakhir ditampilkan

def load_image(path):
    global citra, citra_resized, gray, binary, last_image_shown
    citra = cv2.imread(path)
    if citra is None:
        print("Gagal membuka gambar.")
        return None
    dim = (300, 300)
    citra_resized = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(citra_resized, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    last_image_shown = citra_resized
    return citra_resized

def get_original():
    return citra_resized if citra_resized is not None else warn("Gambar")

def get_binary():
    return binary if binary is not None else warn("Binary")

def get_grayscale():
    return gray if gray is not None else warn("Grayscale")

def get_not():
    return cv2.bitwise_not(binary) if binary is not None else warn("NOT")

def get_sharpen():
    if gray is not None:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(gray, -1, kernel)
    return warn("Sharpen")

def get_brightness():
    return cv2.add(gray, 50) if gray is not None else warn("Brightness")

def get_erosi():
    if binary is not None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        return cv2.erode(binary, kernel, iterations=1)
    return warn("Erosi")

def show_histogram():
    if gray is not None:
        plt.figure("Histogram Grayscale")
        plt.hist(gray.ravel(), 256, [0, 256])
        plt.title("Histogram Grayscale")
        plt.xlabel("Intensitas")
        plt.ylabel("Jumlah Piksel")
        plt.grid()
        plt.show()
    else:
        print("⚠️ Gambar belum dimuat.")

def get_last_image():
    global last_image_shown
    return last_image_shown

def set_last_image(image):
    global last_image_shown
    last_image_shown = image

def warn(nama):
    print(f"⚠️ {nama} belum tersedia. Silakan muat gambar terlebih dahulu.")
    return None
