#! /usr/bin/python3
import os

images = []
for x in os.listdir():
    if x.endswith(".png") or x.endswith(".jpg"):
        images.append(x)

handle = open('index.html', 'w')
for pics in images:
    v = '<a href="'+pics+'"><img src="'+pics+'" width="32" height="32"></a>&nbsp;\n'
    handle.write(v)
handle.close()

