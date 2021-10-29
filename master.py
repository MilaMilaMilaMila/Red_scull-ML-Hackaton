import csv
import json


def get_rectangle(points: list):
    maxi_x, maxi_y = 0, 0
    mini_x, mini_y = 1, 1
    for point in points:
        x, y = point['left'], point['top']
        maxi_x = max(maxi_x, x)
        maxi_y = max(maxi_y, y)
        mini_x = min(mini_x, x)
        mini_y = min(mini_y, y)
    return (mini_x, maxi_x), (mini_y, maxi_y)


with open('train-all.csv', newline='') as csvfile:
    trains = csv.reader(csvfile, delimiter=',')
    with open('train-all-rectangles.csv', 'w', newline='') as csvanswer:
        answriter = csv.writer(csvanswer, delimiter=',')
        answriter.writerow(['id', 'image', 'rectangles'])
        for num,data in enumerate(trains):
            if not num:
                continue
            num = ''.join(data[0])
            rects = []
            load = json.loads('[' + data[2].replace('\\', '') + ']')
            for index in load:
                rects.append(f"{get_rectangle(index['points'])}")
            answriter.writerow([num, data[1], ' '.join(rects)])
