import cx_Oracle
import static_data as sd


connection = cx_Oracle.connect(user=sd.USERNAME, password=sd.PASSWORD,
                               dsn=sd.DSN),

def insert_data(data: dict, connection: cx_Oracle.Connection = connection) -> bool:
    """ To Insert data into the Oracle Database """
    with connection.cursor() as cursor:
        _query = """
            INSERT INTO ADMIN.CHANGE_REQ_TBL(
                REQUEST_DATE, 
                PROJECT_CO_ORDINATOR, 
                PROJECT_NAME, 
                ACTIVITY_DETAILS, 
                IMPACT_SITE_LIST,
                SERVICE_TYPE,
                DOWN_TIME,
                COMMERCIAL_ZONE,
                NCR_NUMBER,
                CHANGE_MANAGER
                STATUS
                )
                VALUES (
                    :REQUEST_DATE, 
                    :PROJECT_CO_ORDINATOR,
                    :PROJECT_NAME,
                    :ACTIVITY_DETAILS,
                    :IMPACT_SITE_LIST,
                    :SERVICE_TYPE,
                    :DOWN_TIME,
                    :COMMERCIAL_ZONE,
                    :NCR_NUMBER,
                    :CHANGE_MANAGER,
                    :STATUS)
                    """
        try:
            cursor.execute(_query, data)
            connection.commit()
            return True
        except Exception as e:
            print(e)
            return False


def extract_data(connection: cx_Oracle.Connection = connection):
    """ To Extract data from the Oracle Database """
    with connection.cursor() as cursor:
        _query = """
            SELECT * FROM ADMIN.CHANGE_REQ_TBL
            """
        cursor.execute(_query)
        return cursor.fetchall()