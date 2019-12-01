from flask import Flask, request
from flask import render_template   # 导入模板渲染模块
import client

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == 'POST':
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        username = request.form["username"]
        # print('name', username)
        # print('温度', temperature)
        # print('湿度', humidity)
        client.send_data("[{},{},{}]".format(username, temperature, humidity))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1314, debug=True)
    # app.run(host='127.0.0.1', port=5000, debug=True)