import pymysql

def commit(sql):
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="test",
        database="myDb",
        charset="utf8",
    )
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    sqls = """  CREATE DATABASE IF NOT EXISTS django; 
                ALTER user 'root'@'localhost' IDENTIFIED BY 'test'; 
                """

    for sql in sqls.split("\n"):
        commit(sql)
