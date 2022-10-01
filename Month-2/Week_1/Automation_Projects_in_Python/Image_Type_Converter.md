### Importing Python Image Library - for Image Processing. 
 ````python
 from PIL import Image
 ````
###  Importing Glob to return all file paths that match a specific pattern.
 ````python
import glob
 ````
 ## Converting Image
 ````python
print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgb_im = im.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=95)


'''
import os
for file in glob.glob("*.jpg"):
    os.remove(file)
'''
````
