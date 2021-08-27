import mysql.connector as mysql
from mysql.connector import errorcode

def create_connection(databases):
    cnx = None
    try:
        cnx = mysql.connect(user='root', password='', database=databases, host="localhost")
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx

def select_bieu_hien(cons,benh):
    if(cons == None):
        return "lỗi server"
    else:
        cur = cons.cursor()
        query = ("SELECT bh.descriptions FROM bieu_hien bh, benh b WHERE b.id_benh = bh.id_benh and b.descroptions like %s Limit 1")
        cur.execute(query,("%" + benh + "%",))
        result = cur.fetchone()
        if (result == ""):
            return "Không có thông tin về biểu hiện bệnh "+ benh
        else:
            return  result[0]
    