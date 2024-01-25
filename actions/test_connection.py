import cx_Oracle

connection = None

sql = 'select PUK2 ' \
    'from SUBSCRIPTION ' \
    'where IMSI=100975100000042'


try:
    with cx_Oracle.connect(user="smapp", password="3928ad5894cf58dc7569ad5b733c85",
                               dsn="acc50-dbh-scan.dcp.fi.eu.xdn.ericsson.se:1521/APCONT_SM_SERVICE",
                               encoding="UTF-8") as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                print(row[0])
        # # show the version of the Oracle Database
        # print(connection.version)
        
except cx_Oracle.Error as error:
    print(error)
        
    
