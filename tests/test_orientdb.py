__author__ = 'lorenzo'

import pyorient
import requests
import demjson
from pprint import pprint
import simplejson as json

resource ="http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=DESCRIBE+%3Chttp://dbpedia.org/resource/Particle_physics%3E&output=application%2Fld%2Bjson"
doc = demjson.decode(requests.get(resource).text)
#pprint(doc)
# demjson.decode(doc)


client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "asdfg")


db_name = "prova"
# CREATE a DB with db_name
# client.db_create(db_name, pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_PLOCAL)

print(client.db_exists(db_name, pyorient.STORAGE_TYPE_MEMORY))

client.db_open(db_name, "root", "asdfg")  # open connection

# CREATE A RECORD
record = {'value': doc}
#cluster_id = client.command("create class DBpedia extends V")
rec_position = client.record_create(b'12', record)

print(rec_position)
# CREATE A CLASS
#client.command("create class Animal extends V")

# Insert a new value
#client.command("insert into Animal set name = 'rat', specie = 'rodent'")

# DROP DB
# client.db_drop(db_name)

client.db_close()







