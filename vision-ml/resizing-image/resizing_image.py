import cv2

def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float (h)
        dim = (int (w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float (w)
        dim = (width, int (h * r))

    # resize the image
    resized = cv2.resize (image, dim, interpolation=inter)

    # return the resized image
    return resized


image = cv2.imread ('Images/t.jpg')
height, width, depth = image.shape
res_image = image_resize (image, 173, 73)

cv2.imshow ('Original', image)
cv2.imshow ('Final', res_image)

# Zoomed image is saved as 'zoom_img.jpg'
cv2.imwrite ('Images_Out/zoomed.jpg', res_image)
cv2.waitKey (0)
cv2.destroyAllWindows ()
