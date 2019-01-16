import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join
import splitImage as si

mypath = "/home/christopher/test_images"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for i in onlyfiles:
    #img = cv.imread(mypath + "/" + i)

    img0, img1, img2 = si.split(mypath + "/" + i)

    img1 = cv.resize(img1.astype(dtype = np.uint8), (200,200), interpolation = cv.INTER_LINEAR)
    img2 = cv.resize(img2.astype(dtype = np.uint8), (200,200), interpolation = cv.INTER_LINEAR)

    img3 = abs(img1 - img2)

    cv.imshow("image", img0)
    cv.imshow("1",cv.resize(img1, (200,200), interpolation = cv.INTER_LINEAR))
    cv.imshow("2",cv.resize(img2, (200,200), interpolation = cv.INTER_LINEAR))
    cv.imshow("3",img3)
    cv.waitKey(0)

cv.waitKey(0)
