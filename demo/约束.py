class BasePlugins(object):

    def process(self):
        raise NotImplementedError("{}中必须实现process方法" .format(self.__class__.__name__))



class DiskPlugin(BasePlugins):
    def paro(self):
        pass

obj = DiskPlugin()
obj.process()