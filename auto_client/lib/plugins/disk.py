from .bash import BasePlugin
class DiskPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self,ssh,hostname):
        return {'disk':'可用20M硬盘'}