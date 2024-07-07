from sqlalchemy import text
from flask import Flask, request, render_template, jsonify

import utils
import pymysql
from flask_sqlalchemy import SQLAlchemy
# 创建一个app对象
# __name__:代表app.py这个模板
app = Flask(__name__)

# 链接数据库
# 在app.config中设置好连接数据库的信息
# 然后使用SQLAlchemy（qpp）创建一个db对象
# SQLAlchemy会自动读取app.config中的连接数据库的信息



# MySQL所在的主机名
HOSTNAME = 'localhost' # 或者127.0.0.1
# 端口号
PORT = 3306
# 连接MySQL的用户名
USERNAME = "root"
# 连接数据库的密码
PASSWORD = "082316"
# 数据库的名称
DATABASE = "tank"
# 设置数据库连接URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:082316@127.0.0.1:3306/tank?charset=utf8mb4'

db = SQLAlchemy(app)



# 判断是否连接到数据库
# with app.app_context():
#     with db.engine.connect() as conn:
#         sql_query = text("select * from men")  # 使用text方法创建可执行对象
#         rs = conn.execute(sql_query)
#
#         print(rs.fetchall())

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)


# user = User(username="侯", password="123123")
with app.app_context(): # 应用上下文的问题
    db.create_all()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建一个路由和视图函数的映射
# / 根路由


# 数据库的增删改查
@app.route('/user/add')
def user_add():
    #创建orm对象
    user = User(username="侯", password="123123")
    user1 = User(username= "zhu", password="3.14159")
    #创建的orm对象添加到db.session中
    db.session.add(user)
    db.session.add(user1)
    db.session.commit()# 将db.session中的改变同步到数据库中
    return "用户创建成功"

@app.route('/user/query')
def user_query():
    # 1.get查找， 根据主键查找
    # user = User.query.get(1)
    # print(f"{user.id}{user.username}")

    # 2. filter_by() 查找 得到的是query类数组
    users = User.query.filter_by(username="zhu")
    for user in users:
        print(user.username)
    return "查找成功"

@app.route('/user/update')
def user_update():
    user = User.query.filter_by(username="zhu").first()#这里类似指针
    user.password = "122222"
    db.session.commit()
    return "修改成功"

@app.route('/user/delete')
def user_delete():
    # 1.查找
    user = User.query.get(1)
    # 2.从db.session()会话中删除
    db.session.delete(user)
    # 提交会话
    db.session.commit()
    return "数据删除成功"

@app.route('/')
def hello_world():  # put application's code here
    return render_template("main.html")

@app.route('/time')
def get_time():

    return utils.get_time()

@app.route('/getleft2')
def get_left2():
    res=[]
    list = utils.get_left2()
    res.append({"value": list[0], "name": '1-50'})
    res.append({"value": list[1], "name": '50-100'})
    res.append({"value": list[2], "name": '100-150'})
    res.append({"value": list[3], "name": '150-200'})
    res.append({"value": list[4], "name": '200以上'})
    return  jsonify({"data": res})

@app.route('/getleft1')
def get_left1():
    return jsonify({"data": utils.get_left1()})

@app.route('/getcenter1')
def get_center():

    return jsonify(utils.get_center1())

@app.route('/update' ,methods=['POST', 'GET'])
def update_user():
    input_string = request.form['input_string']
    print(input_string)
    return input_string


# 1.debug模式
# 1.1 自动加载
# 1.2 运到bug在网页会看到报错的信息

# 2. 修改host:
# 2.1 让其他电脑能访问到我的flask项目

# 3. 修改port端口号:
# 如果5000端口被其它程序占用了可以更改#
# url:http[80] https[443] 端口

@app.route('/index/<int:index_id>')
def index(index_id):
    return "序号%d" % index_id

@app.route('/book/list')
def book_list():
    # argyment 参数   查询字符串的时候传参
    page = request.args.get('page',default=1, type=int)
    return f"您获得的是第{page}页"
if __name__ == '__main__':
    app.run()
