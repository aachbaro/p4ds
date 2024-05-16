import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    new_arr = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    new_arr = 255 - array
    # Image.fromarray(new_arr.astype(np.uint8)).show()
    img = Image.fromarray(new_arr.astype(np.uint8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return new_arr

def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the red channel
    """
    new_arr = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    new_arr[:, :, 1] = 0
    new_arr[:, :, 2] = 0
    new_arr[:, :, 0] = array[:, :, 0]
    img = Image.fromarray(new_arr.astype(np.uint8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return new_arr

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the green channel
    """
    new_arr = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    new_arr[:, :, 0] = 0
    new_arr[:, :, 2] = 0
    new_arr[:, :, 1] = array[:, :, 1]
    img = Image.fromarray(new_arr.astype(np.uint8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return new_arr

def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keeps only the blue channel
    """
    new_arr = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    new_arr[:, :, 0] = 0
    new_arr[:, :, 1] = 0
    new_arr[:, :, 2] = array[:, :, 2]
    img = Image.fromarray(new_arr.astype(np.uint8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    return new_arr

def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Apply a grey filter on the given array
    """
    new_arr = np.zeros((array.shape[0], array.shape[1], 3), dtype=np.uint8)
    red = array[:, :, 0] / 3
    green = array[:, :, 1] / 3
    blue = array[:, :, 2] / 3
    new_arr = red + green + blue
    img = Image.fromarray(new_arr.astype(np.uint8))
    plt.imshow(img, cmap="grey")
    plt.axis('off')
    plt.show()
    return new_arr