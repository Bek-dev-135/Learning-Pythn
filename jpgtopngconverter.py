import sys
import os
from PIL import Image


#fisrst lets take two arguments

image_folder= sys.argv[1]
output_folder= sys.argv[2]

print(image_folder,output_folder)

#check if the folder new exists

if not (os.path.exists(output_folder)):
    os.makedirs(output_folder)


    #lopp throught the file

for filename in os.listdir(image_folder):
    img=Image.open(f'{image_folder}\{filename}')
    clean_name =os.path.splitext(filename)[0]
    img.save(f'{output_folder}\{clean_name}.png ', 'png')
    print('alldone')

