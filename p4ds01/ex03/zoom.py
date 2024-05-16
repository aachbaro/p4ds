from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Shows a truncated version of animal.jpeg"""
    try:
        print(ft_load("animal.jpeg"))
        img = Image.open("animal.jpeg")
        img = img.crop((450, 100, 850, 500))
        img = img.convert("L")
        print(f"New shape after slicing: ({img.size})")
        arr = np.array(img.getdata())
        arr = np.reshape(arr, (img.size[1], img.size[0], 1))
        print(arr)
        plt.imshow(img, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
