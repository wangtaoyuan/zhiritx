# encoding=utf-8
import sqlite3


# 数据库操作
def select_zrtx(sql_words):
    # print(sql_words)
    conn = sqlite3.connect('zrtx.db')
    cursor = conn.cursor()
    cursor.execute(sql_words)
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    if values == []:
        return -1
    else:
        # print(values[0][0])
        return values[0][0]


email_workers = {'常雪松': '626267475@qq.com', '李鑫': '907035184@qq.com',  '王阳': '28700776@qq.com',
                 '颉鑫': '837207831@qq.com', '贾若愚': '672401341@qq.com',  '王涛渊': '846292076@qq.com',
                 '李鹏飞': '1751409741@qq.com', '李佳锦': '972526556@qq.com', '王会月': '1174361204@qq.com',
                 '高靖智': '624823065@qq.com',  '张旭': '664313276@qq.com', '陈秀新': '1665150972@qq.com',
                 '郭佳兴': '1141958382@qq.com'}
if __name__ == '__main__':
    # while True:
    rowid = 1
    for name in email_workers:
        conn = sqlite3.connect('zrtx.db')
        cursor = conn.cursor()
        email = email_workers[name]
        cursor.execute("insert into worker (rowid, name, email) values (\'%d\', \'%s\', '%s')" % (rowid, name, email))
        rowid += 1
        cursor.close()
        conn.commit()
        conn.close()

