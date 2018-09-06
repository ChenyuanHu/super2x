import os
import os.path
import cv2

rootdir = 'image'
newdir = 'new'

g_cnt = 0

def handle(path):
    global g_cnt
    img = cv2.imread(path)

    img = cv2.resize(img, (1440, 900))
    filename = str(g_cnt) + ".jpg"
    cv2.imwrite(os.path.join(newdir, filename), img)

    img = cv2.resize(img, (720, 450))
    filename = str(g_cnt) + "_min.jpg"
    cv2.imwrite(os.path.join(newdir, filename), img)

    g_cnt = g_cnt + 1

for parent, dirnames, filenames in os.walk(rootdir):
    #print(parent, dirnames, filenames)
    for filename in filenames:
        if (filename.endswith(".jpg")):
            path = os.path.join(parent, filename)
            handle(path)