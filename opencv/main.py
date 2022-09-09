import cv2
import numpy as np
from params import read_flags

for key, flag in read_flags.items():
    img = cv2.imread("image1.jpg", flag)
    cv2.imshow(key, img)
    cv2.waitKey()



"""
num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols + 70,
            num_rows + 110), cv2.INTER_LINEAR)

num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1, 0, int(num_cols * 0.5)], [0, 1, num_rows * 0.5]])
rotation_matrix = cv2.getRotationMatrix2D((num_cols, num_rows), 30, 1)

img_translation = cv2.warpAffine(img, translation_matrix, (num_cols * 2,
            num_rows * 2))
img_rotation = cv2.warpAffine(img_translation, rotation_matrix, (num_cols * 2,
            num_rows * 2))
cv2.imshow("affine rotate", img_rotation)

cv2.waitKey()
"""
