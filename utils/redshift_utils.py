import os

import psycopg2


def get_redshift_connector():
    dbname = os.environ('dbname')
    host = os.environ('db_host')
    user = os.environ('db_user')
    passwd = os.environ('db_passwd')
    connector = psycopg2.connect(dbname=dbname,
                                 host=host,
                                 port='5439',
                                 user=user,
                                 password=passwd)
    return connector


def group_exist(group_name):
    # TODO
    # select * from pg_group;
    return False


def create_redshif_group(group_name):
    connector = get_redshift_connector()
    curs = connector.cursor()
    sql_str = 'Create group '+group_name
    curs.execute(sql_str)
    curs.commit()
    curs.close()
    return True
    # create group


def execute_sql(sql_str):
    connector = get_redshift_connector()
    curs = connector.cursor()
    curs.execute(sql_str)
    curs.commit()
    curs.close()
    return None
