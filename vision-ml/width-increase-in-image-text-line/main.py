import cv2
import numpy as np
from skimage.filters import threshold_local, threshold_yen


def show(title: str, imagePath: str):
    """
    Shows the Image with title.
    :param title: Title of Image
    :param image: image read as numpy ndarray e.g. cv2.imread(...)
    :return: nothing
    """
    image = cv2.imread (imagePath)
    cv2.imshow (title, image)


def preprocessor(image_path, binary=True):
    """ Increase Line Width of Handwritten Text => returns image with line width wider"""
    img = cv2.imread (image_path)
    shape = cv2.resize (img, (int (200), int (64))).shape[:2]

    # Binary
    if binary:
        brightness = 0
        contrast = 50
        img = np.int16 (img)
        img = img * (contrast / 127 + 1) - contrast + brightness
        img = np.clip (img, 0, 255)
        img = np.uint8 (img)

        img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
        T = threshold_local (img, 11, offset=10, method="gaussian")
        img = (img > T).astype ("uint8") * 255

        # Increase line width
        kernel = np.ones ((3, 3), np.uint8)
        img = cv2.erode (img, kernel, iterations=1)
    else:
        img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

    return img


old_image_path = "in/f/f15.png"
new_image_path = "out/f15.png"
cv2.imwrite (new_image_path, preprocessor (new_image_path))

show ("Original", old_image_path)
show ("New", new_image_path)

cv2.waitKey (0)
exit (0)
