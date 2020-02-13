from .bash import  BasePlugin
class BasicPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self,ssh,hostname):
        return {'basic': 'hostname-gqa'}


