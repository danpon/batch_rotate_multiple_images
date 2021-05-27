import os
import shutil
import threading
import time
# import the Python Image processing Library
from PIL import Image


input_dir_path="./input"
output_dir_path="./output"
image_name=""
rotation_angle=-90

def rotate_image():  
    print(image_name)
    imageIn  = Image.open(input_dir_path+"/"+image_name)
    imageOut = imageIn.rotate(rotation_angle)   
    imageOut.save(output_dir_path+"/"+image_name) 
    time.sleep(3)

def main():

    # init output dirctory
    try:
        shutil.rmtree(output_dir_path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir_path)


    global image_name
    print("Start...")
    entries=os.listdir(input_dir_path)
    for entry in entries:
        image_name = entry
        #start images rotation thread
        thread = threading.Thread(target=rotate_image)
        thread.start()
        # wait here for the result to be available before continuing
        thread.join()
    print("End.")


if __name__ == '__main__':
    main()