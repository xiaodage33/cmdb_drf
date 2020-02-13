from concurrent.futures import ThreadPoolExecutor

import requests
import paramiko

def ssh(hostname,cmd):


    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=22, username='root', password='Agqa6631')
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    result = stdout.read()
    # 关闭连接
    ssh.close()
    return result
#
# def task(host):
#     server_info = get_server_info(ssh, host)
#     result = requests.post(
#         url='http://127.0.0.1:8000/api/get_data/',
#         json={'host': host, 'info': server_info}
#     )
#     print(result)
#
# def run():
#     pool = ThreadPoolExecutor(10)
#     host_list = [
#         '192.168.14.39',
#         # '192.168.14.37',
#         # '192.168.14.38',
#     ]
#     for host in host_list:
#         pool.submit(task,host)


if __name__ == '__main__':
    data = ssh(hostname = "121.43.187.197", cmd='df -h ')
    print(data)

