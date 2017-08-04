import PIL
import os.path              
import matplotlib.pyplot as plt
import numpy as np

#Rozmy Miranda and Kristina Becht 8-1-17
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
background = os.path.join(directory, 'Bioshock.jpg')

# These will be used to obtain a base PIL image
underwater = PIL.Image.open(background)
underwater = underwater.crop((0,0,1500,900))

# First PIL transformation sets new boundaries for image and distorts a recangular piece
underwater2 = underwater.transform((1000,700), PIL.Image.QUAD, (132,221,135,820,1165,825,1500,900))

# Used this one to rotate the image
underwater3 = underwater2.rotate(68, expand=False)
fig, axes = plt.subplots(1, 4)
axes[0].imshow(underwater, interpolation='none')
axes[1].imshow(underwater2, interpolation='none')
axes[2].imshow(underwater3, interpolation='none')

# Have to save the image as something else to be able to access pixel arrays
underwater3.save('city.jpg')

# Opened up image again using matplot to mess with pixels
City = plt.imread('city.jpg')
height = len(City)
width = len(City[0])

#Lightens center box created by a factor of 3
for r in range(200,500):
    for c in range(400,600):
        if sum(City[r][c]) > 90:
         City[r][c]=City[r][c]*3
         
#Lightens tip left and bottom right boxes by a factor of 6
for r in range(0,200):
    for c in range(0,400):
        if sum(City[r][c]) > 90:
         City[r][c]=City[r][c]*6
for r in range(500,700):
    for c in range(600,1000):
        if sum(City[r][c]) > 90:
         City[r][c]=City[r][c]*6
axes[3].imshow(City, interpolation='none')

fig.show()