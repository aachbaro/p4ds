from PIL import Image
import numpy as np
import os


def ft_load(path: str) -> np.ndarray:
    """Loads an image, print his shape and return his pixel array"""
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        i = Image.open(path)
        arr = np.array(i.getdata())
        arr = np.reshape(arr, (i.size[1], i.size[0], 3))
        print(f"The shape of image is: ({i.size[1]}, {i.size[0]}, {i.layers})")
        return arr
    except Exception as error:
        print("Error:", error)
