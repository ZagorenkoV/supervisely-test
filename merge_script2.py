import numpy as np
import os

path = './sliced_image_image2.jpg/'
# загрузить все нарезанные блоки в список
images_list = []
for address, dirs, files in os.walk(path):
    for name in files:
        images_list.append(os.path.join(address, name))

for x in range(0, 1920, 192):
    row_blocks = []
    for y in range(0, 1080, 108):
        block = np.load(f"image1(from{x,y})to({x+1,y+1}).jpg")
        row_blocks.append(block)
    images_list.append(np.concatenate(row_blocks, axis=1))

# объединить все строки вместе
full_image = np.concatenate(images_list, axis=0)