import csv
import json
from PIL import Image


# before start, you should have three directories
# train/ (with photos from the drone)
# cutted/ (directory for the positive result)
# leaved/ (directory for the negative result)
class HeapOfGarbage:
    def __init__(self, minx, maxx, miny, maxy, width, height):
        self.coordinates = (minx * width, miny * height, maxx * width, maxy * height)

    def __contains__(self, item):
        if item[2] > self.coordinates[0] > item[0] and item[3] > self.coordinates[1] > item[1]:
            return True
        if self.coordinates[2] > item[0] > self.coordinates[0] and self.coordinates[3] > item[1] > self.coordinates[1]:
            return True
        if item[2] > self.coordinates[0] and self.coordinates[1] > item[1] > self.coordinates[3] > item[3]:
            return True
        if item[0] > self.coordinates[0] > self.coordinates[2] > item[2] and \
                self.coordinates[1] < item[1] < self.coordinates[3] < item[3]:
            return True
        if item[1] > self.coordinates[1] > self.coordinates[3] > item[3] and \
                self.coordinates[0] < item[0] < self.coordinates[1] < item[1]:
            return True
        return False


def cut_rest(n, filepath, coords: list):
    filename = get_image_address(filepath)
    im = Image.open(f"train/{filename}")
    sizex, sizey = im.size
    heap = HeapOfGarbage(*coords, sizex, sizey)
    counter = 1
    step = 800
    for maxi_x in range(step, sizex, step):
        for maxi_y in range(step, sizey, step):
            mini_x, mini_y = maxi_x - step, maxi_y - step
            if (mini_x, mini_y, maxi_x, maxi_y) not in heap:
                cropped_im = im.crop((mini_x, mini_y, maxi_x, maxi_y))
                cropped_im.save(f"leaved/{filename.split('.')[0]}-CUT_terrace-{counter}.{filename.split('.')[1]}")
                """
                csvout = open('train-all-terrace.csv', 'a', newline='')
                answriter = csv.writer(csvout, delimiter=',')
                answriter.writerow([str(n), filepath, '[' + f'{mini_x}, {maxi_x}, {mini_y}, {maxi_y}' + ']'])
                csvout.close()
                counter += 1
                """
    im.close()


def cut_garbage(filename, coords: list, number_of_heap):
    im = Image.open(f"train/{filename}")
    heap = HeapOfGarbage(*coords, *im.size)
    cropped_im = im.crop(heap.coordinates)
    name, ext = filename.split('.')
    cropped_im.save(f"cutted/{name}-CUT_garbage-{number_of_heap + 1}.{ext}")
    im.close()


with open('train-all-rectangles.csv', 'r', newline='') as csvfile:
    """
    csvout = open('train-all-terrace.csv', 'w', newline='')
    answriter = csv.writer(csvout, delimiter=',')
    answriter.writerow(['id', 'image', 'square'])
    csvout.close()
    """
    imgs = csv.reader(csvfile, delimiter=',')
    get_image_address = lambda x: x.split('/')[-1]
    for num, img in enumerate(imgs):
        if not num:
            continue
        data = json.loads(img[2])
        for n, heap in enumerate(data['points']):
            cut_garbage(get_image_address(img[1]), heap, n)
        if len(data['points']) == 1:
            cut_rest(num, img[1], data['points'][0])

