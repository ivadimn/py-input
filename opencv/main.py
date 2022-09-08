import cv2
import numpy as np

img = cv2.imread("IMG_3930.JPG", cv2.IMREAD_COLOR)
g, b, r = cv2.split(img)
#yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
gbr_img = cv2.merge((g, b, r))
rbr_img = cv2.merge((r, b, r))
cv2.imshow("original image", img)
cv2.waitKey()
cv2.imshow("gbr image", gbr_img)
cv2.waitKey()
cv2.imshow("rbr image", rbr_img)
cv2.waitKey()
#print([x for x in dir(cv2) if x.startswith('COLOR_')])


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

