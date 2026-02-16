
from PIL import Image
import os

images = ['superstore_1.png', 'superstore_2.png', 'superstore_3.png']
images_list = [Image.open(x) for x in images]

# Assuming all images have the same width, if not, resize them to the max width
widths, heights = zip(*(i.size for i in images_list))

max_width = max(widths)
total_height = sum(heights)

new_im = Image.new('RGB', (max_width, total_height))

y_offset = 0
for im in images_list:
  # If images are different widths, center them or resize. For simplicity, we just paste.
  # If resizing is needed:
  if im.size[0] != max_width:
      new_height = int(im.size[1] * (max_width / im.size[0]))
      im = im.resize((max_width, new_height), Image.Resampling.LANCZOS)
      
  new_im.paste(im, (0, y_offset))
  y_offset += im.size[1]

new_im.save('Superstore_Combine.png')
print("Image combined successfully!")
