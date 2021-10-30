import csv
import json

with open('train-all-rectangles.csv', 'r', newline='') as csvin:
    with open('train-all-rectangles-prettify.csv', 'w', newline='') as csvout:
        ins = csv.reader(csvin, delimiter=',')
        outs = csv.writer(csvout, delimiter=',')
        outs.writerow(['id','image','rectangles'])
        for count, line in enumerate(ins):
            if not count:
                continue
            n, link, rects = line
            data = json.loads(rects)
            for rect in data['points']:
                outs.writerow([n, link, rect])
