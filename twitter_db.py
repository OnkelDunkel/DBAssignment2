








import requests, zipfile, io, pprint, pymongo, csv

dowload_url = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
file_name = "testdata.manual.2009.06.14.csv"


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["twitterdb"]
db2 = db["twitterdb"]
db2.insert_one({"bob":"bob"})
print("listing dbs")
print(myclient.list_database_names())



def retrieve_file():
    try:
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("-downloading twitter data")
        r = requests.get(dowload_url, stream=True)
        print("-creating zip file")
        z = zipfile.ZipFile(io.BytesIO(r.content))
        print("-extracting zip file")
        z.extractall()
        print("-data was retrieved succesfully")

def add_data_to_db():
    csv.register_dialect("goo")
    with open(file_name, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            #pprint.pprint(row)
            print(row[3])
            if not len(row) == 6:
                print(row)




    '''
    f = open(file_name, "r")
    while f.
    for i in range(0,10):
    f.readline())
    '''


#retrieve_file()
#add_data_to_db()