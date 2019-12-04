from flask import Flask, request
from flask import render_template   # 导入模板渲染模块
import client

from socket import *
import threading

app = Flask(__name__)

"""
定义文件传输类:
类名： Data_transmission
类属性：data : 传输的消息 数据类型：列表 [['name'], ['温度'], ['湿度']]
类方法：send_data : 
类方法：add_data: 接收数据并预备发送
类方法：server ： 开启服务，接收客户端请求, 接收客户端的数据请求并响应给客户端服务器数据，每当响应一个数据就将当前数据从列表中删除
"""
class Data_transmission(object):
    def __init__(self):
        self.data = []

    def send_data(self):
        pass

    def add_data(self, receive_data):
        self.data.append(receive_data)
    
    def server(self):
        # 1 创建套接字
        tcp_server_socket = socket(AF_INET, SOCK_STREAM)

        # 2 bind 绑定 IP 和 port
        # tcp_server_socket.bind(("192.168.149.1", 7891))   # 0.0.0.0 表示任何客户端都可连接
        # tcp_server_socket.bind(("192.168.136.1", 7891))
        tcp_server_socket.bind(("47.95.118.108", 7891))
        
        # 3 listen 使套接字变为被动链接
        tcp_server_socket.listen(128)

        # 4 accept 等待客户端的链接 返回值（新套接字：为客户端服务，客户端信息）
        while True:
            print("等待客户端连接中...")
            new_socket, addr = tcp_server_socket.accept()  # 堵塞状态
            print("客户端已连接...")
     
            # 5 接收发送数据
            while True:
                try:
                    recv_data = new_socket.recv(1024)   # 接受客户端的请求 最大 1024 接收二进制字节流
                    
                    print(recv_data.decode("gbk"))   # 解码并打印

                    if recv_data.decode("gbk") == "hcasjaasfc":   # 结束服务
                        return 

                    if recv_data:
                        # new_socket.send("**ok**".encode("gbk"))   # 回复客户端表示收到请求
                        if self.data == []:
                            break
                        else:
                            send_data = self.data[0]
                            new_socket.send(send_data.encode("gbk"))
                            self.data.pop(0)
                            break
                    else:
                        break
                except:
                    break
     
            # 6 关闭 accept 返回的套接字 表示不再为该客户端服务
            new_socket.close()
        # 关闭 tcp_server_socket 套接字
        tcp_server_socket.close()

# 实例化对象
A = Data_transmission()
# A.add_data("sb941")




@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == 'POST':
        temperature = request.form["temperature"]
        humidity = request.form["humidity"]
        username = request.form["username"]
        print('name', username)
        print('温度', temperature)
        print('湿度', humidity)

        # client.send_data("[{},{},{}]".format(username, temperature, humidity))
        data = "[{},{},{}]".format(username, temperature, humidity)

        A.add_data(data)

        A.data = list(set(A.data))

        print(A.data)

    # 实例化线程
    a = threading.Thread(target=A.server)
    a.start()

    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7890, debug=True)
    # app.run(host='192.168.149.1', port=7890, debug=True)
    # app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(debug=False)