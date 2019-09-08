import requests
from .sql import SqlServer


class APIAccess():
    def __init__(self, sql_table, sql_db, sql_user, sql_password, sql_address):
        self.server = SqlServer(sql_address, sql_user, sql_password, sql_db)
        self.table = sql_table
    
    def get(self, query, base_url):
        cached_searches = []
        complete_url = base_url + query.replace(' ','+')
        print("Query URL: ", complete_url)

        cached_searches_obj = self.server.get_by_column(self.table, "search_url")
        for entry in cached_searches_obj:
            entry_data = "{}".format(entry)
            entry_data = entry_data.replace(',', '')
            entry_data = entry_data.replace('(', '')
            entry_data = entry_data.replace(')', '')
            entry_data = entry_data.replace('\'', '')
            cached_searches.append(entry_data)

        print("Fetched cached searches, there are {} of them".format(len(cached_searches)))
        #print(cached_searches)
        if complete_url in cached_searches:
            print("Grabbing from SQL..")
            for item in cached_searches:
                if item == complete_url:
                    return self.server.search(self.table, "search_url", item)
                    break
        else:
            print("Grabbing from web...")
            with requests.get(complete_url) as socket:
                json_data = socket.json()
                raw_data = socket.text
            self.server.insert(self.table, ['search_query', 'json_data', 'search_url'], [query, raw_data, complete_url])
            return json_data

