# from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def transpose(arr: np.ndarray) -> np.ndarray:
    """
    Transpose an array
    ARGS:
        arr (np.ndarray): the array to transpose
    RETURNS:
        (np.ndarray): the array transposed
    """
    new_arr = np.zeros((arr.shape[0], arr.shape[1]), dtype=int)
    for columns in range(arr.shape[0]):
        for rows in range(arr.shape[1]):
            new_arr[rows][columns] = arr[columns][rows]
    return new_arr


def main():
    """Loads animal.jpeg, crop it then rotate it"""
    try:
        img = Image.open("asnimal.jpeg")
        img = img.crop((450, 100, 850, 500))
        img = img.convert("L")
        print(f"The shape of image is: ({img.size})")
        arr = np.array(img.getdata(), dtype=np.uint8)
        arr = np.reshape(arr, (img.size[1], img.size[0], 1))
        print(arr)
        print(f"New shape after Transpose: ({img.size})")
        arr = np.reshape(arr, (img.size[1], img.size[0]))
        arr = transpose(arr)
        print(arr)
        image = Image.fromarray(arr.astype(np.uint8))
        plt.imshow(image, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except Exception as error:
        print("Error: ", error)


if __name__ == "__main__":
    main()
