import importlib
from setting import PLUGIN_CLASS_DICT
import setting

# def get_server_info():
    # server_info = {}
    # for key, path in PLUGIN_CLASS_DICT.items():
    #     modeule_path, class_name = path.rsplit('.', maxsplit=1)
    #     module = importlib.import_module(modeule_path)
    #     cls = getattr(module, class_name)
    #     plugin_object = cls()
    #     info = plugin_object.process()
    #     server_info[key] = info
    # return server_info



    # for key, path in PLUGIN_CLASS_DICT.items():
    #     server_info = {}
    #     print(key,path)
    #     modeule_path, class_name = path.rsplit('.', maxsplit=1)
    #     modeul = importlib.import_module(modeule_path)
    #     cls = getattr(modeul,class_name)
    #     plugin_object = cls()
    #     info = plugin_object.process()
    #     print(info)
    #     server_info[key] = info
    #     print('-----------------')
    #     return server_info

# def get_server_info():
#     server_info = {}
#     for key, path in PLUGIN_CLASS_DICT.items():
#         modeule_path, class_name = path.rsplit('.', maxsplit=1)
#         module = importlib.import_module(modeule_path)
#         cls = getattr(module, class_name)
#         plugin_object = cls()
#         info = plugin_object.process()
#         server_info[key] = info
#         return server_info

def get_server_info(ssh,hostname):
    server_info = {}
    for key,path in setting.PLUGIN_CLASS_DICT.items():
        module_path,class_name = path.rsplit('.',maxsplit=1)
        module = importlib.import_module(module_path)
        cls = getattr(module,class_name)
        plugin_object =cls()
        info = plugin_object.process(ssh,hostname)
        server_info[key] = info
    return server_info
