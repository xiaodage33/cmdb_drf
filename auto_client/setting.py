# PLUGIN_CLASS_DICT= {
#     'disk': '硬盘可用量100M',
#     'network': '网卡信息为 10.0.0.51',
#     'menary':'内存信息为可用10M'
# }
PLUGIN_CLASS_DICT = {
    "disk": 'lib.plugins.disk.DiskPlugin',
    'memory': 'lib.plugins.memory.MemoryPlugin',
    'network': 'lib.plugins.network.NetworkPlugin',
    'basic': 'lib.plugins.basic.BasicPlugin',
}
PORT = 22
USENAME = 'root'
PASSWD = 'Agqa6631'