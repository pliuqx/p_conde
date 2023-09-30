# -*- coding:utf-8 -*-
# @Time : 2022/1/5 14:40
# @Author: 应无所住，何生其心
# @File : MysqlSave.py
# @Software : PyCharm
import pymysql

def txt_save(datalist):
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    cursor.execute('use xs')
    sql = ("insert into xhaoxu(txt) values(%s)")
    for i in datalist:
        cursor.execute(sql, (i))
        conn.commit()
    conn.close()
    print(datalist)
