import os

from log.logger import logger
import urllib.parse
# import boto3
import pandas
import io

# from botocore.exceptions import ClientError
from utils.redshift_utils import RedshiftUtils

my_logger = logger()
# s3_resource = boto3.resource("s3", region_name="cn-north-1")
# 要读取的Excel 中的列
TARGET_COL = (
    'AD Group Name', 'Redshift Group', 'User Permission', 'Schema', 'Entity Type', 'Entity Name', 'RLS Row',
    'RLS Column')


def lambda_handler(event, context):
    # 从S3 bucket 读取目标文件
    # bucket = event['Records'][0]['s3']['bucket']['name']
    # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        '''
        response = s3_resource.get_object(Bucket=bucket, Key=key)
        body = response['Body']
        excel_string = body.read()
        df = pandas.read_excel(io.BytesIO(excel_string),
                               sheet_name='')
        '''
        ## 读取Excel 中 指定的sheet，该sheet 包含权限相关信息
        df = pandas.read_excel('Redshift Permission Template.xlsx', sheet_name='Group Permission Templete',
                               index_col=TARGET_COL[1])
        redshiftUtils = RedshiftUtils()
        for index, row in df.iterrows():
            my_logger.info(f'Redshift Group Name: {index}')
            ## 检查 redshif 组是否已经创建，如果未创建则执行 create group
            if not redshiftUtils.group_exist(index):
                my_logger.info(f'Grouo not exist, will create..')
                redshiftUtils.create_redshif_group(index)
            user_permission = row[TARGET_COL[2]].replace('/', '|')
            my_logger.info(user_permission)
            entity_type = row[TARGET_COL[4]]
            entity_name = row[TARGET_COL[5]]
            schema = row[TARGET_COL[3]]
            grant_sql_str = 'Grant '
            if entity_type == 'All':
                grant_sql_str = grant_sql_str + user_permission + ' IN SCHEMA' + schema
            else:
                grant_sql_str = grant_sql_str + user_permission + ' IN SCHEMA' + schema
            my_logger.info(f"SQL to be executed: {grant_sql_str}")
            redshiftUtils.execute_sql(grant_sql_str)
            rls_row =  row[TARGET_COL[6]]
            rls_colum = row[TARGET_COL[6]]
            my_logger.info(rls_row)
            my_logger.info(rls_colum)
            # TODO
            rls_sql_str = rls_row + rls_colum ## to be confirmed
            redshiftUtils.execute_sql(rls_sql_str)
    except Exception as e:
        my_logger.error(e)
        raise e


if __name__ == '__main__':
    lambda_handler(None, None)
