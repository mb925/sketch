# This is a sample Python script.
import os
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
    input = '/home/martina/PycharmProjects/sketch/input'
    rename = '/home/martina/PycharmProjects/sketch/rename'
    files = os.listdir(input)
    for index, file in enumerate(files):
        os.rename(os.path.join(input, file), os.path.join(rename, f'Human Face #{index+1}.jpg'))


def metamask(driver):

    SECRET_RECOVERY_PHRASE = ''
    NEW_PASSWORD = ''


    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > div > button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > div.select-action__wrapper > div > div.select-action__select-buttons > div:nth-child(1) > button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > div > div.metametrics-opt-in__footer > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > form > div.first-time-flow__textarea-wrapper > div.MuiFormControl-root.MuiTextField-root.first-time-flow__textarea.first-time-flow__seedphrase > div > input'
    driver.find_element(By.CSS_SELECTOR, css).send_keys(SECRET_RECOVERY_PHRASE)
    time.sleep(2)

    css = '#password'
    driver.find_element(By.CSS_SELECTOR, css).send_keys(NEW_PASSWORD)
    time.sleep(2)

    css = '#confirm-password'
    driver.find_element(By.CSS_SELECTOR, css).send_keys(NEW_PASSWORD)
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > form > div.first-time-flow__checkbox-container > div'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > form > button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div > button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

def driver_exec():
    print(Path.home())
    EXTENSION_PATH = '/home/martina/.config/google-chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.5.2_0.crx'
    DRIVER_PATH = '/home/martina/PycharmProjects/sketch/chromedriver'
    print(EXTENSION_PATH)

    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=opt)

    driver.switch_to.window(driver.window_handles[0])
    metamask(driver)
    driver.switch_to.window(driver.window_handles[-1])

    driver.get('https://opensea.io/collection/face-of-humanity/assets/create')
    time.sleep(5)

    # print(driver.window_handles)

    css = '#__next > div.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.FlexColumnreact__FlexColumn-sc-1wwz3hp-0.OpenSeaPagereact__DivContainer-sc-65pnmt-0.dBFmez.jYqxGr.ksFzlZ.fiudwD > main > div > div > div > div.Blockreact__Block-sc-1xf18x6-0.eOSaGo > ul > li:nth-child(1) > button > div.Blockreact__Block-sc-1xf18x6-0.Flexreact__Flex-sc-1twd32i-0.FlexColumnreact__FlexColumn-sc-1wwz3hp-0.VerticalAlignedreact__VerticalAligned-sc-b4hiel-0.Itemreact__ItemContent-sc-1idymv7-1.dBFmez.jYqxGr.ksFzlZ.iXcsEj.hTefVc'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[-1])

    css = '#app-content > div > div.main-container-wrapper > div > div.permissions-connect-choose-account > div.permissions-connect-choose-account__footer-container > div.permissions-connect-choose-account__bottom-buttons > button.button.btn--rounded.btn-primary'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(2)

    css = '#app-content > div > div.main-container-wrapper > div > div.page-container.permission-approval-container > div.permission-approval-container__footers > div.page-container__footer > footer > button.button.btn--rounded.btn-primary.page-container__footer-button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[-1])

    css = '#app-content > div > div.main-container-wrapper > div > div.request-signature__footer > button.button.btn--rounded.btn-primary.btn--large.request-signature__footer__sign-button'
    driver.find_element(By.CSS_SELECTOR, css).click()
    time.sleep(5)

    # print(driver.window_handles)

    # driver.close()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function call
    rename()

    for filename in os.listdir('rename'):
        print(filename)

        image = cv2.imread(f'rename/{filename}')
        resized_image = resizeImage(image)
        coloured = ColorQuantization(resized_image)
        contoured = findCountours(coloured)
        final_image = contoured
        cv2.imwrite('output_640x860/' + filename, final_image)
        print("Image saved!")

    # driver_exec()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
