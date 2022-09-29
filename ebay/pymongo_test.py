from pymongo import MongoClient

#MONGO DB CONNECTION
username="ebay-django-db"
password = "E8KiR0WoJ8IACyKe"
connect_string  =f"mongodb+srv://{username}:{password}@cluster0.cly8mna.mongodb.net/?retryWrites=true&w=majority"
my_client = MongoClient(connect_string)
# First define the database name
dbname = my_client["tea-party"]
# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
collection_name = dbname["user-login"]

sellerInfo ={'UserID': 'desert_valley_goods', 'Email': 'pablogeorgeporras@gmail.com', 'MaxScheduledItems': '3000', 'PositiveFeedbackPercent': '100.0', 'FeedbackScore': '3', 'UniquePositiveFeedbackCount': '3', 'UniqueNegativeFeedbackCount': '0'}

key = {'UserID':'desert_valley_goods'}


collection_name.update_one(key,{"$set":sellerInfo},upsert=True)


