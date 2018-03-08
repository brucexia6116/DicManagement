from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from models import *
from models import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# 词典整合测试程序
@app.route('/')
def hello_world():
    id_list = Tab01.query.order_by(Tab01.id).all()
    l1 = len(id_list)  # 获取表1的长度
    # print(l1)
    id_list02 = Tab02.query.order_by(Tab02.id).all()
    l2 = len(id_list02)  # 获取表2的长度
    # print(l2)
    for i in range(1, l1 + 1):  # 循环遍历表1，得到每一条记录
        dis1 = Tab01.query.filter_by(id=i).first()
        # print("i:", i)
        # print(dis1)
        for j in range(1, l2 + 1):  # 循环遍历表2得到每一条记录
            dis2 = Tab02.query.filter_by(id=j).first()
            # print(dis2)
            # print("j:", j)
            if dis2.diseasename == dis1.diseasename:  # 判断表1读取的术语名称与表2读取的术语名称是否相等
                dis1.description = dis2.description  # 术语名称相等，则将表2的描述信息复制给表1
                db.session.commit()

    for k in range(1, l2 + 1):  # 循环遍历表2
        dis3 = Tab02.query.filter_by(id=k).first()  # 读取表2中的每一条数据
        print("k:", k)
        print("表2：", dis3)
        for n in range(1, l1 + 1):  # 循环遍历表1
            dis4 = Tab01.query.filter_by(diseasename=dis3.diseasename).first()  # 利用读取的表2的术语名称查询表1
            if dis4 is None:  # 如果查询结果为空
                newDis = Tab01(code=dis3.code, diseasename=dis3.diseasename,
                               description=dis3.description)  # 将表2中的该条数据添加到表1
                db.session.add(newDis)
                db.session.commit()
            # print("表1：",dis4)
            # if dis4.diseasename == dis3.diseasename:
            #     # newDis = Tab01(code=dis3.code, diseasename=dis3.diseasename, description=dis3.description)
            #     # db.session.add(newDis)
            #     # db.session.delete(dis3)
            #     # db.session.commit()
            #     break
            # dis5=Tab01.query.order_by(Tab01.id).all()
            # print("表1：",dis5)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
