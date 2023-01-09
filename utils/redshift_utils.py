import os

import psycopg2


class RedshiftUtils:
    def __init__(self):
        dbname = os.environ('dbname')
        host = os.environ('db_host')
        user = os.environ('db_user')
        passwd = os.environ('db_passwd')
        connector = psycopg2.connect(dbname=dbname,
                                     host=host,
                                     port='5439',
                                     user=user,
                                     password=passwd)
        self.curs = connector.cursor()

    def group_exist(self, group_name):
        # TODO
        # select * from pg_group;
        return False

    def create_redshif_group(self, group_name):
        sql_str = 'Create group ' + group_name
        self.curs.execute(sql_str)
        self.curs.commit()
        self.curs.close()
        return True
        # create group

    def execute_sql(self, sql_str):
        self.curs.execute(sql_str)
        self.curs.commit()
        self.curs.close()
        return None

    def execute_query(self, sql_str):
        list_result = ()
        try:
            self.cursor.execute(sql_str)
            list_result = self.cursor.fetchall()
            self.cursor.close()
        except Exception as e:
            print(e)
        return list_result



