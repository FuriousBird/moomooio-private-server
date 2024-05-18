# Description: This script downloads all the resources from the moomoo.io website.
# author    : FuriousBird
# date      : 2021/03/01
# version   : 1.0.0

import json, os, time
import urllib.error
import urllib.request

testfile = urllib.request.URLopener()
testfile.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
testfile.addheader('Referer', 'https://moomoo.io/')
testfile.addheader('Origin', 'https://moomoo.io/')
testfile.addheader('Host', 'moomoo.io')
testfile.addheader('Connection', 'keep-alive')
testfile.addheader('Accept-Encoding', 'gzip, deflate, br')
testfile.addheader('Accept-Language', 'en-US,en;q=0.9')

SKIP_DONE = True
if SKIP_DONE:
    print("WARNING: Skipping enabled, will not download files that already exist.")
    time.sleep(2)

skipdest = lambda dest: os.path.exists(dest) and SKIP_DONE

with open("data2download.json", "rb") as f:
    data = json.loads(f.read().decode("utf-8"))

#data has keys groups, projectiles, weapons, and list
def imjoin(path):
    return "img/"+path

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

print("# DOWNLOADING ICONS")
BASEPATH = imjoin("icons")
os.makedirs(BASEPATH, exist_ok=True)
for icon in ["skull", "crown"]:
    
    dest = BASEPATH+"/"+icon + ".png"
    if skipdest(dest):
        continue
    src = "https://moomoo.io/"+dest
    print(src)
    testfile.retrieve(src, dest)

print("# DOWNLOADING WEAPONS")
BASEPATH = imjoin("weapons")
os.makedirs(BASEPATH, exist_ok=True)
for wep in data["weapons"]:
    if not wep.get("src", False):
        continue
    for suffix in ["", "_g", "_d", "_r", "_e"]:
        dest = BASEPATH+"/"+wep["src"] +suffix+ ".png"
        if skipdest(dest):
            continue
        src = "https://moomoo.io/"+dest
        print(src)
        try:
            testfile.retrieve(src, dest)
        except urllib.error.HTTPError as e:
            if e.status == 404:
                print("Missing:", src)

print("# DOWNLOADING PROJECTILES")
BASEPATH = imjoin("weapons")
os.makedirs(BASEPATH, exist_ok=True)
for proj in data["projectiles"]:
    if not proj.get("src", False):
        continue
    dest = BASEPATH+"/"+proj["src"] + ".png"
    if skipdest(dest):
        continue
    src = "https://moomoo.io/"+dest
    print(src)
    testfile.retrieve(src, dest)

with open("hats2download.json", "rb") as f:
    data = json.loads(f.read().decode("utf-8"))

#downlaod all hats
print("# DOWNLOADING HATS")
BASEPATH = imjoin("hats")
os.makedirs(BASEPATH, exist_ok=True)
for hat in data["hats"]:
    if not hat.get("id", False):
        continue
    dest = BASEPATH+"/"+"hat_"+str(hat["id"]) + ".png"
    if skipdest(dest):
        continue
    src = "https://moomoo.io/"+dest
    print(src)
    testfile.retrieve(src, dest)

#download all accessories
print("# DOWNLOADING ACCESSORIES")
BASEPATH = imjoin("accessories")
os.makedirs(BASEPATH, exist_ok=True)
for acc in data["accessories"]:
    if not acc.get("id", False):
        continue
    dest = BASEPATH+"/"+"access_"+str(acc["id"]) + ".png"
    if skipdest(dest):
        continue
    src = "https://moomoo.io/"+dest
    print(src)
    testfile.retrieve(src, dest)

with open("aitypes.json", "rb") as f:
    data = json.loads(f.read().decode("utf-8"))

#downlaod all animals
print("# DOWNLOADING HATS")
BASEPATH = imjoin("animals")
os.makedirs(BASEPATH, exist_ok=True)
for animal in data:
    dest = BASEPATH+"/"+animal["src"] + ".png"
    if skipdest(dest):
        continue
    src = "https://moomoo.io/"+dest
    print(src)
    testfile.retrieve(src, dest)




