import cv2
import os

name = 'image'
exten = '.jpg'
img = cv2.imread(f'./{name}{exten}')
yy = 0
crop_img_height = 180
crop_img_width = 320
row_counter = 0
for row in range(int(img.shape[0] / crop_img_height)):
    column_counter = 0
    xx = 0
    for column in range(int(img.shape[1] / crop_img_width)):
        crop_img = img[yy: yy + crop_img_height, xx: xx + crop_img_width]
        img_name = name + '(' + str(crop_img_width * (column_counter)) + '-' + \
                   str(crop_img_width * (column_counter + 1)) + '-' + str(crop_img_height * (row_counter)) + '-' + \
                   str(crop_img_height * (row_counter + 1)) + exten
        if not os.path.exists("sliced_images"):
            os.makedirs("sliced_images")
        cv2.imwrite(f"sliced_images/{img_name}", crop_img)
        column_counter += 1
        xx += crop_img_width
        cv2.waitKey(0)
    row_counter += 1
    yy += crop_img_height