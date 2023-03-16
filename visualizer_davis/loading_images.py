import os

path = 'C:\Projects\supervisely\DAVIS\JPEGImages\1080p'

if os.path.exists(path):
    root, folders, files = next(os.walk(path))
   
# (assuming we have > 42 images) we can get the full path for a file by:
filepath = os.path.join(root, files)