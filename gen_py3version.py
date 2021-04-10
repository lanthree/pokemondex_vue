# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import json
import sys
import os
import re
import time
import pypinyin
import html2text
import random

# import sys

# defaultencoding = "utf-8"
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)


def ParseTr(tr):
    tds = tr.select("td")

    icon_idx = 0
    for idx in range(0, len(tds)):
        if len(tds[idx].select("span")) == 1:
            icon_idx = idx
            break

    no_td = tds[icon_idx - 1]
    wiki_td = tds[icon_idx + 1]
    no = no_td.get_text().strip()
    name = wiki_td.select("a")[0].get_text()
    url = wiki_td.select("a")[0].get("href")

    types = []
    for idx in range(0, len(tds)):
        if (
            "class" in tds[idx].attrs
            and "textwhite" in tds[idx]["class"]
            and "hide" not in tds[idx]["class"]
        ):
            types.append(tds[idx].get_text().strip())

    return no, name, url, types


def ParsePokeDoc(url):

    response = requests.get("https://wiki.52poke.com/{}".format(url))
    response.enconding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    content_node = (
        soup.body.select(".mw-body")[0]
        .select("#bodyContent")[0]
        .select("#mw-content-text")[0]
        .select(".mw-parser-output")[0]
    )

    out_content = ""
    c = content_node.select(".mw-headline")[0].parent.next_sibling
    while True:
        out_content += str(c)
        c = c.next_sibling
        if c.name == "h2":
            break

    out_content = re.sub(r"href", "none", out_content)
    out_content = re.sub(r"<dl.+dl>", "", out_content)
    out_content = html2text.html2text(out_content)

    ss = [
        int(content_node.select('tr[class="bgl-HP"] div')[1].get_text()),
        int(content_node.select('tr[class="bgl-特攻"] div')[1].get_text()),
        int(content_node.select('tr[class="bgl-特防"] div')[1].get_text()),
        int(content_node.select('tr[class="bgl-速度"] div')[1].get_text()),
        int(content_node.select('tr[class="bgl-防御"] div')[1].get_text()),
        int(content_node.select('tr[class="bgl-攻击"] div')[1].get_text()),
    ]

    print("ParsePokeDoc ok")
    return out_content, ss


def GetOfficalInfo(no):
    response = requests.get("https://cn.portal-pokemon.com/play/pokedex/{}".format(no))
    response.enconding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    img_url_base = "https://cn.portal-pokemon.com"
    urls = []
    for div in soup.body.select(".pokemon-style-box"):
        url = img_url_base + div.a.img.get("src")
        urls.append(url)

    if len(urls) == 0:
        url = img_url_base + soup.body.select(".pokemon-img__front")[0].get("src")
        urls.append(url)

    story = soup.body.select(".pokemon-story__body")[0].get_text().strip()

    print("GetOfficalInfo ok")
    return urls, story


def GetPinyinFirstLetter(name):
    s = ""
    for i in pypinyin.pinyin(name, style=pypinyin.FIRST_LETTER):
        s += "".join(i)
    return s


def AddTypes(doc_file_path, types):
    f = open(doc_file_path, "r")
    data = f.read()
    f.close()

    obj = json.loads(data[20:])
    # if obj.has_key("types"):
    if "types" in obj:
        return

    obj["types"] = types
    SaveObj(doc_file_path, obj)
    print("AddTypes ", doc_file_path)


def SaveObj(doc_file_path, obj):
    obj_js = json.dumps(obj)

    fo = open(doc_file_path, "w")
    fo.write("export const data = {}".format(obj_js))
    fo.close()


response = requests.get(
    "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"
)
response.enconding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

body_tag = soup.body
eplist = (
    body_tag.select(".mw-body")[0]
    .select("#bodyContent")[0]
    .select("#mw-content-text")[0]
    .select(".mw-parser-output")[0]
    .select(".eplist")
)


global count
count = 0


def GetCount():
    global count
    count += 1
    return count


is_retry = True

indexes = []
for ep in eplist:
    area = ep.select("tbody tr th a")[0].get_text().split("（")[0]
    indexes_ep = {"id": GetCount(), "label": area + "图鉴", "children": []}

    trs = ep.tbody.select("tr")
    for idx in range(2, len(trs)):

        no, name, url, types = ParseTr(trs[idx])
        title = no + " " + name
        bid = no[1:]

        doc_file_path = "./src/assets/data/{}.js".format(bid)

        pinyin = GetPinyinFirstLetter(name)
        index_item = {
            "id": GetCount(),
            "label": title,
            "bid": no[1:],
            "match": no + " " + name + " " + pinyin + " " + pinyin.upper(),
        }
        indexes_ep["children"].append(index_item)

        if is_retry and os.path.exists(doc_file_path):
            AddTypes(doc_file_path, types)
            print("skip ", title)
            continue

        print("===== {} start downloading".format(title))

        try:
            content, ss = ParsePokeDoc(url)
            urls, story = GetOfficalInfo(bid)
            data = {
                "bid": bid,
                "name": name,
                "content": content,
                "urls": urls,
                "story": story,
                "ss": ss,
                "types": types,
            }
            SaveObj(doc_file_path, data)
            print("===== {} done".format(title))
        except IOError as e:
            print("===== error ", no[1:], e)
            pass

        time.sleep(4)

    indexes.append(indexes_ep)

doc_file_path = "./src/assets/data/indexes.js"
SaveObj(doc_file_path, indexes)