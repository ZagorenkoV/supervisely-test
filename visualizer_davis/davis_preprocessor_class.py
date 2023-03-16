import os
import cv2
from random import shuffle


class DAVISDataPreprocessor(object):
    def __init__(self, path_to_input_images, path_to_output_videos):
        if not os.path.exists(path_to_input_images) or not os.path.exists(path_to_output_videos):
            raise ValueError('path(s) doesn\'t exist!')
        
        # extract the filenames of the images (input)
        self.input_root, input_folders, _ = next(os.walk(path_to_input_images))
        self.videos_input = {}
        for video_foldername in input_folders:
            video_path = os.path.join(self.input_root, video_foldername)
            if os.path.exists(video_path):
                _, _, images = next(os.walk(video_path))
                self.videos_input[video_foldername] = images
        
        # repeat for output images
        self.output_root, output_folders, _ = next(os.walk(path_to_output_videos))
        self.videos_output = {}
        for video_foldername in input_folders:
            video_path = os.path.join(self.input_root, video_foldername)
            if os.path.exists(video_path):
                _, _, images = next(os.walk(video_path))
                self.videos_input[video_foldername] = images

    def load_image_from_file(self, filename):
        filepath = os.path.join(self.input_root, filename)
        
        return cv2.imread(filepath)
    
    def load_mask_from_file(self, filename):
        filepath = os.path.join(self.output_root, filename)
        
        raw_mask = cv2.imread(filepath)
        
        # do further processing on `raw_mask`
        
        return raw_mask
                
    def generate_data(self):
        # initialize variables as needed
        images = []
        for image_list in self.videos_input.values():
            images.extend(image_list)

        masks = []
        for mask_list in self.videos_output.values():
            masks.extend(mask_list)

        i = 0
        # may need to shuffle dataset
        shuffle(images)

        while True:
              # may need to detect if we've gone through the entire dataset and reshuffle
              if i >= len(images):
                  shuffle(images)
                  i = 0

              # grab next inputs and outputs
              next_input = self.load_image_from_file(images[i])
              next_output = self.load_mask_from_file(masks[i])

              # perform data augmentation as needed
              # do any other preprocessing steps

              yield next_input, next_output

              i += 1