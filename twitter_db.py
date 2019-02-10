import requests, zipfile, io, pprint, pymongo, csv, re

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = myclient["twitter_db"]
tweets = db["tweets"]

for tweet in tweets.find():
    linked_users = []
    for match in re.finditer("(^|\\s)@(\\w+)", tweet["text"]):
        linked_users.append(match.group(2))
    tweet["linked_users"] = linked_users
    tweets.save(tweet)

def find_user_count():
    user_count = len(tweets.distinct("user"))
    print("\n\nuser count:")
    print(str(user_count))

def find_user_linking_to_others():
    user_who_links = tweets.aggregate([
        {"$unwind":"$linked_users"},
        {"$group":{"_id":"$user", "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":10},
    ])
    print("\nmost linking to other user")
    pprint.pprint(list(user_who_links))


def find_most_linked_users():
    most_linked_users = tweets.aggregate([
        {"$unwind":"$linked_users"},
        {"$group":{"_id":"$linked_users", "count":{"$sum":1}}},
        {"$sort":{"count":-1}},
        {"$limit":5},
    ])
    print("\nmost mentioned users")
    pprint.pprint(list(most_linked_users))

def find_most_active():
    most_active = tweets.aggregate([
        {"$group":{"_id":"$user", "tweet_count":{"$sum":1}}},
        {"$sort":{"tweet_count":-1}},
        {"$limit":10},
    ])
    print("\nmost active")
    pprint.pprint(list(most_active))

def find_most_grumpy():
    most_active = tweets.aggregate([
        {"$group":{"_id":"$user", "grumpyness":{"$avg":"$polarity"}}},
        {"$sort":{"grumpyness":1}},
        {"$limit":5},
    ])
    print("\nmost grumpy")
    pprint.pprint(list(most_active))

find_user_count()
find_user_linking_to_others()
find_most_linked_users()
find_most_active()
find_most_grumpy()
print("done")
