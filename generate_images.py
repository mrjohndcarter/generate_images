"""Simple script to generate images for testing."""
# This script randomly crops images of a specified size from a file randomly
# selected from a specified directory.
#
# Requires:
#    - PIL
#
# Usage:
#   python generate_images.py W H NUMBER FORMAT DIRECTORY
#
# Arguments (all required)
#    W - Width of the images to generate.
#    H - Height of the images to generate.
#    NUMBER - Number of images to generate.
#    FORMAT - Format of images to generate ('png' or 'jpg').
#    DIRECTORY - Path to directory to read images from.
#
# Example Usage:
#   python generate_images.py 100 100 10 png ./imgs

import sys
import Image # PIL

from os import listdir
from os.path import join
from random import randint
from random import choice

def random_crop(width, height, image):
    """Crops a random region of width x height from image.
    Returns an image"""
    crop_origin_x = randint(0, image.size[0] - width)
    crop_origin_y = randint(0, image.size[1] - height)
    crop_box = (crop_origin_x, \
        crop_origin_y, \
        crop_origin_x + width, \
        crop_origin_y + height)
    return image.crop(crop_box)

def main():
    """Entry point function."""
    if (len(sys.argv) != 6):
        print '\nUsage: \n\t' + sys.argv[0] + """ WIDTH HEIGHT \
        (NUMBER OF IMAGES TO CREATE) (png | jpg) \
        (DIRECTORY TO READ IMAGES FROM)\n"""
        sys.exit(0)

    image_count = int(sys.argv[3])+1

    for i in range(1, image_count):
        print 'Generating image ' + str(i) + ' of ' + str(image_count)
        source_filename = join(sys.argv[5], choice(listdir(sys.argv[5])))
        output_image = random_crop(int(sys.argv[1]),
            int(sys.argv[2]),
            Image.open(source_filename))
        output_image.save('.'.join([str(i), sys.argv[4]]))

if __name__ == "__main__":
    main()
