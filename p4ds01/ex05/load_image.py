from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    i = Image.open(path)
    arr = np.array(i.getdata(), dtype=np.uint8)
    arr = np.reshape(arr, (i.size[1], i.size[0], 3))
    print(f"The shape of image is: ({i.size[1]}, {i.size[0]}, {i.layers})")
    print(arr)
    return arr
