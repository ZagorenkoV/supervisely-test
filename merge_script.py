import os
import numpy as np
from PIL import Image

def join_sliced_image(image_name, wind_width, wind_height, step_x, step_y):
    if not os.path.exists(f"sliced_image_{image_name}"):
        return print(f"No sliced images found for {image_name}")
    
    sliced_images = os.listdir(f"sliced_image_{image_name}")
    sliced_images.sort()
    
    num_rows = ((Image.open(f"sliced_image_{image_name}/{sliced_images[0]}").size[1] - wind_height) // step_y) + 1
    num_cols = ((Image.open(f"sliced_image_{image_name}/{sliced_images[0]}").size[0] - wind_width) // step_x) + 1
    
    joined_image = np.zeros((num_rows * wind_height, num_cols * wind_width, 3), dtype=np.uint8)
    
    for i in range(num_rows):
        for j in range(num_cols):
            img_path = f"sliced_image_{image_name}/{image_name[:-4]}(form({j*step_x},{i*step_y})to({j*step_x+wind_width},{i*step_y+wind_height})).jpg"
            img = Image.open(img_path)
            img_arr = np.asarray(img)
            joined_image[i*wind_height:(i+1)*wind_height, j*wind_width:(j+1)*wind_width, :] = img_arr
    
    Image.fromarray(joined_image).save(f"joined_{image_name}")
    print(f"Sliced images have been successfully joined to 'joined_{image_name}'")