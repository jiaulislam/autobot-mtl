import datetime
from typing import List, Tuple
import cx_Oracle

USERNAME = 'admin'
PASSWORD = 'admin123'
DSN = 'localhost:1521/cidb'

connection: cx_Oracle.Connection = cx_Oracle.connect(
    user=USERNAME, password=PASSWORD, dsn=DSN)


def insert_data(data: dict, connection: cx_Oracle.Connection = connection) -> bool:
    """ To Insert data into the Oracle Database """
    with connection.cursor() as cursor:
        _query = """INSERT INTO ADMIN.CHANGE_REQ_TBL(
            REQUEST_DATE, PROJECT_CO_ORDINATOR, PROJECT_NAME, ACTIVITY_DETAILS, IMPACT_SITE_LIST, SERVICE_TYPE, DOWN_TIME, COMMERCIAL_ZONE, NCR_NUMBER, CHANGE_MANAGER, STATUS)
                    VALUES(:REQUEST_DATE, :PROJECT_CO_ORDINATOR, :PROJECT_NAME, :ACTIVITY_DETAILS, :IMPACT_SITE_LIST, : SERVICE_TYPE, : DOWN_TIME, : COMMERCIAL_ZONE, : NCR_NUMBER, : CHANGE_MANAGER, : STATUS)"""
        try:
            cursor.execute(_query, data)
            connection.commit()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            return False


def extract_data(date: str = str(datetime.date.today().strftime('%d-%b-%y')), connection: cx_Oracle.Connection = connection):
    """ To extract data from the Oracle Database """
    with connection.cursor() as cursor:
        _query = """
            SELECT * FROM ADMIN.CHANGE_REQ_TBL WHERE REQUEST_DATE=:REQUEST_DATE
            """
        try:
            cursor.execute(_query, REQUEST_DATE=date)
            return cursor.fetchall()
        except cx_Oracle.DatabaseError as e:
            raise e


def export_data(date: str = str(datetime.date.today().strftime('%d-%b-%y')), connection: cx_Oracle.Connection = connection, cr_status: str ='REQUEST FOR AUTHORIZATION') -> List:
    """ To export data as a formatted xlsx output file """
    with connection.cursor() as cursor:
        _query = """ SELECT * FROM ADMIN.CHANGE_REQ_TBL WHERE REQUEST_DATE=:REQ_DATE AND STATUS=:cr_status ORDER BY SLNO ASC """

        try:
            cursor.execute(_query, REQ_DATE=date, cr_status=cr_status)
            return cursor.fetchall()
        except cx_Oracle.DatabaseError as e:
            raise e


def update_data(data: dict, connection: cx_Oracle.Connection = connection):
    """ To update data in the Oracle Database """
    # ! need to complete below code for update 
    with connection.cursor() as cursor:
        _query = """UPDATE ADMIN.CHANGE_REQ_TBL SET STATUS = :STATUS WHERE REQUEST_ID = :REQUEST_ID"""
        try:
            cursor.execute(_query, data)
            connection.commit()
            return True
        except cx_Oracle.DatabaseError as e:
            print(e)
            return False
            