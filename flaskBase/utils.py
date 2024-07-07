import time

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")

def get_conn():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='082316',
                           charset='utf8',
                           db='tank')
    cursor = conn.cursor()
    return conn, cursor
def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query_db(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    close_conn(conn, cursor)
    return result

def get_left2():
    sql = "select 价格 from dangdangwang"
    result = query_db(sql)
    prices = [row[0] for row in result]
    list = [0,0,0,0,0]
    for price in prices:
        if price<50:
            list[0]+=1
        elif price >= 50 and price < 100:
            list[1] += 1
        elif price >= 50 and price < 100:
            list[2] += 1
        elif price >= 100 and price < 150:
            list[3] += 1
        elif price >= 200:
            list[4] += 1

    return list
def get_left1():
    sql = "select 价格 from dangdangwang"
    result = query_db(sql)
    prices = [row[0] for row in result]
    return prices


def get_center1():
    sql = "select 价格 from dangdangwang"
    result = query_db(sql)
    prices = [row[0] for row in result]
    res = []
    list = [0, 0, 0, 0]
    list[0] = max(prices)
    list[1] = min(prices)
    list[2] = int(sum(prices) / len(prices))
    list[3] = int(sum(prices))
    res.append({"max":list[0]})
    res.append({"min": list[1]})
    res.append({"avg": list[2]})
    res.append({"sum": list[3]})
    return res
if __name__ == '__main__':
   print(get_center1())