import json
import pandas as pd
with open('response.json','r') as file:
    data = json.load(file)

#['data']['contentLayout']['modules']['configs']['products']
for item in data['data']['contentLayout']['modules'][0]['configs']['products']:
    print(item['name'])
    print(item['availabilityStatus'])
    print(item['averageRating'])
    print(item['fulfillmentTitle'])
    print(item['imageInfo']['thumbnailUrl'])
    print(item['numberOfReviews'])
    print(item['priceInfo'])
