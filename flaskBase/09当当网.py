import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import pymysql
# 连接到你的 MySQL 数据库
header = {
    "ser-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "Cookie":"__permanent_id=20240614183029961166257261309619833; secret_key=ff87491b4760f1b60e75dfa64730429f; ddscreen=2; __visit_id=20240618091631662277235568622241190; __out_refer=1718673392%7C!%7Cwww.baidu.com%7C!%7C; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_9_end=1718674015298; __rpm=%7Cs_605252.451999115329%2C451999115330.1.1718674016689; ad_ids=3554365%2C2533482%2C2092059%7C%232%2C2%2C1; __trace_id=20240618092658019258201542402506028; pos_1_start=1718674018517; pos_1_end=1718674018526",
    "Referer":"https://product.dangdang.com/1437396929.html"
}



def get_area(url,header):
    encodings = 'utf-8'
    area_sourse = requests.get(url, headers=header).text
    area_page = BeautifulSoup(area_sourse, "html.parser")
    area = area_page.find("div", attrs={"class":"select_add clearfix"}).find('span').text
    return area


mydb = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='082316',
    database='tank'
)
mycursor = mydb.cursor()
#
# # 检查表格是否存在
# mycursor.execute("SHOW TABLES LIKE 'dangdangwang'")
# result = mycursor.fetchone()
#
# # 准备数据
# if result:
#     print("Table already exists. Skipping table creation.")
# else:
#     # 创建一个表格
#     mycursor.execute("CREATE TABLE DangDangWang (名称 VARCHAR(255), 链接 VARCHAR(255), 价格 FLOAT)")
#     print("Table created successfully.")
#     mydb.commit()

url = "https://search.dangdang.com/?key=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&page_index=1"
res = requests.get(url)
encodings = "utf-8"
main_mage_sourse = res.text
main_page = BeautifulSoup(main_mage_sourse, "html.parser")
lis = main_page.find("ul",attrs={"class":"bigimg cloth_shoplist"}).find_all("li")
for li in lis:
    title = li.find("a").get("title")
    href = urljoin("https://product.dangdang.com/",li.find("a").get("href"))

    if href.endswith(".html"):
        price = li.find("span", attrs={"class": "price_n"}).text
        price =float(''.join(filter(lambda x: x.isdigit() or x == '.', price)))
        item = (title, href, price)
        print(href)
        time.sleep(1)
        print(get_area(href,header))
    break
        # mycursor.execute("INSERT INTO DangDangWang (名称, 链接, 价格) VALUES (%s, %s, %s)", item)
        # mydb.commit()
# mycursor.close()
# mydb.close()