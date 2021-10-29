from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r'input.jpg')

res = img.filter(ImageFilter.CONTOUR)

res.save('result.png')

print('Execution is finished')