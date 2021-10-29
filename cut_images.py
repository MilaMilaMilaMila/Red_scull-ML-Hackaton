import csv, json
from PIL import Image


# before start, you should create two directories
# train/ (with photos from the drone)
# cutted/ (directory for the result)
class HeapOfGarbage:
    def __init__(self, minx, maxx, miny, maxy, width, height):
        self.coordinates = (minx * width, miny * height, maxx * width, maxy * height)


def cut_garbage(filename, coords: list, number_of_heap):
    im = Image.open(f"train/{filename}")
    heap = HeapOfGarbage(*coords, *im.size)
    cropped_im = im.crop(heap.coordinates)
    name, ext = filename.split('.')
    cropped_im.save(f"cutted/{name}-CUT_garbage-{number_of_heap + 1}.{ext}")


with open('train-all-rectangles.csv', 'r', newline='') as csvfile:
    imgs = csv.reader(csvfile, delimiter=',')
    get_image_address = lambda x: x.split('/')[-1]
    for num, img in enumerate(imgs):
        if not num:
            continue
        data = json.loads(img[2])
        for n, heap in enumerate(data['points']):
            cut_garbage(get_image_address(img[1]), heap, n)
