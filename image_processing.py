import cv2
import numpy as np

# Variabel Global
citra = None
citra_resized = None
gray = None
binary = None

def load_image(path):
    global citra, citra_resized, gray, binary
    citra = cv2.imread(path)
    if citra is None:
        print("Gagal membuka gambar.")
        return None
    dim = (300, 300)
    citra_resized = cv2.resize(citra, dim, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(citra_resized, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return citra_resized

def get_original():
    return citra_resized

def get_binary():
    return binary

def get_grayscale():
    return gray

def get_not():
    if binary is not None:
        return cv2.bitwise_not(binary)

def get_sharpen():
    if gray is not None:
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(gray, -1, kernel)

def get_brightness():
    if gray is not None:
        return cv2.add(gray, 50)

def get_erosi():
    if binary is not None:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        return cv2.erode(binary, kernel, iterations=1)

def get_gray_histogram():
    return gray
