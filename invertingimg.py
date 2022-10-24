from PIL import Image

# numpy for performing batch processing and elementwise
# matrix operations efficiently
import numpy as np


# Opening an image, and saving open image object
img = Image.open(r"sample.jpg")

# Creating an numpy array out of the image object
img_arry = np.array(img)

# Maximum intensity value of the color mode
I_max = 255

# Subtracting 255 (max value possible in a given image
# channel) from each pixel values and storing the result
img_arry = I_max - img_arry

# Creating an image object from the resultant numpy array
inverted_img = Image.fromarray(img_arry)

# Saving the image under the name Image_negative.jpg
inverted_img.save(r"Image_negative.jpg")
