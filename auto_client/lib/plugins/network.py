from .bash import BasePlugin


class NetworkPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self,ssh,hostname):
        rel = ssh(hostname,'ip a')
        rel = rel.decode('utf-8')
        return rel
