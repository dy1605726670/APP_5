from socket import *
 
# 客户端
# 发送数据

def send_data(data):
    # 1 创建tcp套接字
    tcp_socket = socket(AF_INET, SOCK_STREAM)
 
    # 2 链接服务器 
    # host = "192.168.149.1"
    host = "47.95.118.108"
    port = 7891
    tcp_socket.connect((host, port))
 
    # 3 发送数据  hcasjaasfc :关闭服务
    send_data = data

    # 编码为二进制字节流发送
    tcp_socket.send(send_data.encode("gbk"))

    r = tcp_socket.recv(1024)

    print(r.decode("gbk"))
 
    # 4 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    data = "444"
    send_data(data)
