from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open(r'input.jpg')

img.save('result.png')

print('Execution is finished')