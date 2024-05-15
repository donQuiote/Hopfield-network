import matplotlib.pyplot as plt
import os
from skimage.filters import threshold_otsu
from skimage import io
from skimage.color import rgb2gray, rgba2rgb
from skimage import transform

def image_reformer(image_name = 'yoshi.png'):
    #Fetches the file in Images
    filename = os.path.join(os.path.abspath('Visuals/Images'), image_name)
    #Checks whether the file exists
    if not os.path.isfile(filename):
        raise NameError("The file doesn't exist, please check that the file is in the Images file or select an existing file")
    #reads the image
    image = io.imread(filename)

    grayscale = transform.resize(rgb2gray(rgba2rgb(image)),(100,100), anti_aliasing=True)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    ax = axes.ravel()

    ax[0].imshow(image)
    ax[0].set_title("Original")
    ax[1].imshow(grayscale, cmap=plt.cm.gray)
    ax[1].set_title("Grayscale")

    fig.tight_layout()
    plt.show()


    thresh = threshold_otsu(grayscale)
    binary = grayscale > thresh

    fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1)
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

    ax[0].imshow(grayscale, cmap=plt.cm.gray)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram')
    ax[1].axvline(thresh, color='r')

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title('Thresholded')
    ax[2].axis('off')

    plt.show()
    return(binary)
