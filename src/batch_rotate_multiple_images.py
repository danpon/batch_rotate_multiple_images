import os
import shutil
# import the Python Image processing Library
from PIL import Image


input_dir_path="./input"
output_dir_path="./output"
image_name=""
rotation_angle=-90

def rotate_image(image_name):  
    print(image_name)
    imageIn  = Image.open(input_dir_path+"/"+image_name)
    imageOut = imageIn.rotate(rotation_angle)   
    imageOut.save(output_dir_path+"/"+image_name) 


def main():
    try:
        shutil.rmtree(output_dir_path)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    os.mkdir(output_dir_path)

    print("Start...")
    entries=os.listdir(input_dir_path)
    for entry in entries:
        rotate_image(entry)
    print("End.")


if __name__ == '__main__':
    main()