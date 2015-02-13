import os
import json
from pprint import pprint
#[os.rename(f, f.replace('py', 'json')) for f in os.listdir('.')]

#for f in os.listdir('.'):
#    with open(f) as fi:
#       data = fi.read()
       
d = '1957.json'
dict_from_file = []
with open(d, 'r', encoding="utf8") as inf:
    dict_from_file.append(json.loads(inf.read()))    

pprint(dict_from_file)
