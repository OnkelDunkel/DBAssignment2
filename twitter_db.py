

'''
The data is a CSV with emoticons removed. Data file format has 6 fields:
0 - the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
1 - the id of the tweet (2087)
2 - the date of the tweet (Sat May 16 23:58:44 UTC 2009)
3 - the query (lyx). If there is no query, then this value is NO_QUERY.
4 - the user that tweeted (robotickilldozr)
5 - the text of the tweet (Lyx is cool)
'''





import requests, zipfile, io, pprint, pymongo, csv, re

dowload_url = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
file_name = "testdata.manual.2009.06.14.csv"

'''
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["twitterdb"]
db2 = db["twitterdb"]
db2.insert_one({"bob":"bob"})
print("listing dbs")
print(myclient.list_database_names())
'''





'''
* How many Twitter users are in the database?
* Which Twitter users link the most to other Twitter users? (Provide the top ten.)
* Who is are the most mentioned Twitter users? (Provide the top five.)
* Who are the most active Twitter users (top ten)?
* Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?
'''

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["twitter_db"]
#db = myclient["twitter_test_db"]
tweets = db["tweets"]

def find_user_count:
    user_count = len(tweets.distinct("user"))
    print("User count:")
    print(str(user_count))

def find_user_linking_to_others:
    user_who_links = tweets.aggregate([
        {"$match":{"text":{"$regex": "(^|\\s)@\\w+(\\s|$)"}}},
        {"$group":{"_id":"$user", "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":10},
    ])
    print("\ntop most linking")
    pprint.pprint(list(user_who_links))


def find_most_linked_users:

    for tweet in tweets.find():
        linked_users = []
        for match in re.finditer("(^|\\s)@(\\w+)", tweet["text"]):
            linked_users.append(match.group(2))
        tweet["linked_users"] = linked_users
        tweets.save(tweet)
        
    most_linked_users = tweets.aggregate([
        {"$unwind":"$linked_users"},
        {"$group":{"_id":"$linked_users", "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":5},
    ])
    print("\nmost mentioned users")
    pprint.pprint(list(most_linked_users))


print("done")


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