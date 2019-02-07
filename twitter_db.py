








import requests, zipfile, io, pprint, pymongo
from pymongo import MongoClient

dowload_url = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
print("downloading")
r = requests.get(dowload_url, stream=True)
print("downloaded")
z = zipfile.ZipFile(io.BytesIO(r.content))
print("extracting")
z.extractall()
print("done")