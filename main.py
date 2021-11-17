# This is a sample Python script.
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def resizeImage(image):
    scale_ratio = 2
    width = 640
    height = 860
    new_dimensions = (width, height)
    resized = cv2.resize(image, new_dimensions, interpolation = cv2.INTER_AREA)

    return resized

def findCountours(image):

    contoured_image = image
    gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 100)
    contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(contoured_image, contours, contourIdx=-1, color=1, thickness=1)
    return contoured_image

def ColorQuantization(image, K=4):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
    compactness, label, center = cv2.kmeans(Z, K, None, criteria, 1, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((image.shape))

    return res2


def img2sketch(photo, k_size):
    # Read Image
    img = cv2.imread(photo)

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    # invert_img=255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), 0)

    # Invert Blurred Image
    invblur_img = cv2.bitwise_not(blur_img)
    # invblur_img=255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
    #
    # Save Sketch
    cv2.imwrite('sketch.png', sketch_img)
    #
    # # Display sketch
    # cv2.imshow('sketch image', sketch_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def rename():
    path = '/home/martina/PycharmProjects/sketch/input'
    files = os.listdir(path)
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, f'Human Face {index+1}.jpg'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function call
    rename()

    # for filename in os.listdir('input'):
    #     print(filename)
    #
    #     image = cv2.imread(f'input/{filename}')
    #     resized_image = resizeImage(image)
    #     coloured = ColorQuantization(resized_image)
    #     contoured = findCountours(coloured)
    #     final_image = contoured
    #     cv2.imwrite('output_640x860/' + filename, final_image)
    #     print("Image saved!")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
