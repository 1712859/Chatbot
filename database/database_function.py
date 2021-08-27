import mysql.connector as mysql

def create_connection(databases):
    cnx = None
    try:
        cnx = mysql.connect(
        user='root', password='',
        host='localhost',
        database= databases)
    except Error as e:
        print(e)
    return cnx

def select_bieu_hien(cons,benh):
    cur = cons.cursor()
    query = ("SELECT bh.descriptions FROM bieu_hien bh, benh b WHERE b.id_benh = bh.id_benh and b.descroptions like %s Limit 1")
    cur.execute(query,("%" + benh + "%",))

    result = cur.fetchone()
    if (result == None | result == ""):
        return "Không có thông tin về biểu hiện bệnh "+ benh
    else:
        return  result
    

