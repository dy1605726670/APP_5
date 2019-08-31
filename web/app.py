# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
import connection_mongodb   # 导入数据库操作

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    my_database = connection_mongodb.My_db()   # 连接数据库等
    data = my_database.query()

    # 将多个参数放进一个字典
    context = {
        "temperature" : data["temperature"],
        "humidity" : data["humidity"]
    }

    return render_template('index.html', name=name,**context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)