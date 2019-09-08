import mysql.connector
class SqlServer():
    def __init__(self, server, username, password, database):
        self.db = mysql.connector.connect(host=server, user=username, passwd=password, database=database)
        self.cursor = self.db.cursor()

    def get_all(self, table):
        self.cursor.execute("SELECT * FROM {}".format(table))
        return self.cursor.fetchall()

    def get_by_column(self, table, *args):
        arg_list = ""
        for arg in args:
            arg_list += arg + ","
        arg_list = arg_list.strip(",")
        self.cursor.execute("SELECT {} FROM {}".format(arg_list, table))
        return self.cursor.fetchall()
    
    def insert(self, table, rows_list, data_list):
        print("Inserting data into {}".format(table))
        datas_list = []
        row_names = ""

        for row in rows_list:
            row_names += row + ","

        for item in data_list:
            datas_list.append(item)

        row_names = row_names.strip(',')
        data_tuple = tuple(data_list)

        val_data = ("%s," * len(data_list)).strip(',')
        print("Values template: ", val_data)
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, row_names, val_data)
        print("Command: ", sql)
        self.cursor.execute(sql, data_tuple)
        self.db.commit()
        print("Done.")

    def search(self, table, column, search_term):
        sql = "SELECT * FROM {} WHERE {} ='{}'".format(table, column, search_term)
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def search_int(self, table, column, search_term):
        sql = "SELECT * FROM {} WHERE {} ={}".format(table, column, search_term)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

        