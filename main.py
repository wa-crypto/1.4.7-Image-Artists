`from PIL import Image, ImageDraw, ImageFilter

image = Image.open('OriginalImages/family_1.jpg')
image.thumbnail((200, 200))
image.save('OriginalImages/family_1.jpg')



im1 = Image.open('OriginalImages/result1.jpg')
im2 = Image.open('OriginalImages/family_1.jpg')

mask_im = Image.new("L", im2.size, 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((600, 50, 800, 250), fill=255)
mask_im.save('OriginalImages/circle.jpg', quality=95)

mask_im_blur = mask_im.filter(ImageFilter.GaussianBlur(10))
mask_im_blur.save('circle_blur.jpg', quality=95)

back_im = im1.copy()
back_im.paste(im2, (0, 0), mask_im_blur)
back_im.save('OriginalImages/result2.jpg', quality=95)
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'result2.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()
fig.savefig('result2graph.jpg')


