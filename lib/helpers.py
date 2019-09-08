from .sql import SqlServer

class Helpers():

    def __init__(self, server, username, password, database):
        self.server = SqlServer(server, username, password, database)

    def find_lat(self, table, lat):
        all_data_list = []
        all_data = self.server.get_all(table)
        for entry in all_data:
            code_type, name, lat, lon, timedate = entry
            all_data_list.append(['type':code_type, 'name':name, 'lat':lat, 'lon':lon, 'time':timedate])

        for item in all_data_list:
            if item 

