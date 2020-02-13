from .bash import  BasePlugin
class MemoryPlugin(BasePlugin):
    '''
    采集内存信息
    '''

    def process(self,ssh,hostnam):
        return {'menory': '可用内存为10G'}