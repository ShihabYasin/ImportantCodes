from PIL import Image
import cv2
import numpy as np
import shutil


def rotate_img(img_path, rt_degr):
    img = Image.open (img_path)
    return img.rotate (rt_degr)


img_ini = cv2.imread ("images/clear.png")
cv2.imshow ('Original', img_ini)

shutil.copy ('images/clear.png', 'image_photoshop/test_0.png')

img_rt_90 = rotate_img ("image_photoshop/test_0.png", 270)
img_rt_90.save ('image_photoshop/test.png')

size = 10  # Speed

img = cv2.imread ("images/test.png")

# generating the kernel
kernel_motion_blur = np.zeros ((size, size))
kernel_motion_blur[int ((size - 1) / 2), :] = np.ones (size)
kernel_motion_blur = kernel_motion_blur / size

# applying the kernel to the input image
output = cv2.filter2D (img, -1, kernel_motion_blur)

cv2.imwrite ('images/test_out.png', output)

img_rt_90 = rotate_img ('images/test_out.png', 90)
img_rt_90.save ('images/test_final.png')

img_final = cv2.imread ("images/test_final.png")
cv2.imshow ('Motion Blur', img_final)

cv2.waitKey (0)

exit (0)
