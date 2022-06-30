import pymysql

class ConnectDataBase():
    def __init__(self,info):
        self.cursor = info.cursor()
        self.info=info
    def Upload_Data(self,HOST,ip,text):
        sql='''INSERT INTO log1 (HOST,IPv4_Adress,Key_Log,UpDate_to_Database)
               VALUES('{}','{}','{}',NOW());'''.format(str(HOST),str(ip),str(text))
        self.cursor.execute(sql)
        self.info.commit()
























        pymysql