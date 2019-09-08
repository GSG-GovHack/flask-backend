import requests

query = "kangaroo"

base_url = "https://bie-ws.ala.org.au/ws/search.json?q="

complete_url = base_url + query.replace(' ','+')
search_items = []

print("Query URL: ", complete_url)

with requests.get(complete_url) as socket:
    json_data = socket.json()

print("Found {} entries".format(json_data['searchResults']['totalRecords']))
results = json_data['searchResults']['results']

for i in range(len(results)):
    print(results[i]['id'])
    search_items.append(results[i])

for item in search_items:
    print(item['name'])

