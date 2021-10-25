import os
import sys
from PIL import Image
for folder_name in os.listdir('.'):
    if folder_name != "combine.py":
        for file_name in os.listdir(f'./{folder_name}'):
            print(os.listdir(f'./{folder_name}/{file_name}'))
            images = [Image.open(f'./{folder_name}/{file_name}/{x}') for x in os.listdir(f'./{folder_name}/{file_name}')]
            widths, heights = zip(*(i.size for i in images))

            total_width = max(widths)
            max_height = sum(heights)

            new_im = Image.new('RGB', (total_width, max_height))

            y_offset = 0
            for im in images:
              new_im.paste(im, (0,y_offset))
              y_offset += im.size[1]

            new_im.save(f'${filename}.png')
