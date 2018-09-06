import os
import os.path
import cv2
import tensorflow as tf


class ImgSet:
    img_dir = 'new'
    cnt = 0

    x_path_array = []
    y_path_array = []
    def init(self):
        for parent, _, filenames in os.walk(self.img_dir):
            #print(parent, dirnames, filenames)
            for filename in filenames:
                if (filename.endswith('_min.jpg')):
                    path = os.path.join(parent, filename)
                    self.y_path_array.append(path)
                    self.x_path_array.append(path.replace('_min', ''))
        

    def next_train_batch(self):
        img = cv2.imread(self.x_path_array[0])
        return img.shape
                

img = ImgSet()
img.init()

#print(img.x_path_array)
#print(img.y_path_array)
print(img.next_train_batch())