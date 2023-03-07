import argparse
from PIL import Image
import matplotlib.pylab
import numpy as np
import skimage
import scipy.ndimage
from skimage.morphology import binary_erosion

threshold = 0.25


def reduce_colors(input_file, output_file):
    print('processing: ' + input_file)

    # convert to grayscale
    img_1 = Image.open(input_file).convert('L')
    width = img_1.width
    height = img_1.height
    img_1.save(output_file + '_1.png')
    print('grayscale: ' + output_file + '_1.png')

    # convert to notan
    img_1 = matplotlib.image.imread(output_file + '_1.png')
    img_2 = np.zeros([height, width], dtype='float')
    for i in range(height):
        for j in range(width):
            img_2[i][j] = 1 if img_1[i][j] > threshold else 0
    matplotlib.image.imsave(output_file + '_2.png', img_2, cmap='Greys_r', vmin=0, vmax=1)
    print('notan: ' + output_file + '_2.png')

    # apply erosion
    img_3 = skimage.img_as_float(img_2)
    struct1 = scipy.ndimage.generate_binary_structure(2, 6)
    img_4 = binary_erosion(img_3, struct1)
    matplotlib.image.imsave(output_file + '_3.png', img_4, cmap='Greys_r', vmin=0, vmax=1)
    print('eroded notan: ' + output_file + '_3.png')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="file path to input image")
    parser.add_argument("output_file", nargs='?', default='img', help="file path to output image, no extension")
    args = parser.parse_args()
    reduce_colors(args.input_file, args.output_file)
