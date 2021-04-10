# -*- coding: utf-8 -*-

import requests
from urllib.request import urlretrieve
import json
import os

for id in range(1, 2): #899
    bid = '%03d' % id
    doc_file_path = "./src/assets/data/{}.js".format(bid)

    f = open(doc_file_path, "r")
    data = f.read()
    f.close()

    obj = json.loads(data[20:])
    for url in obj["urls"]:
        img_file_path = "./data/big/" + url.split('/')[-1]
        
        if os.path.exists(img_file_path):
            print("skip ", img_file_path)
            continue

        urlretrieve(url, img_file_path)