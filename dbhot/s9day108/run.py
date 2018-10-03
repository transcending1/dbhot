
path = "auth.crsf.CORS"


import importlib

module_path,class_name = path.rsplit('.',maxsplit=1)

# 根据字符串的形式导入模块
m = importlib.import_module(module_path)

cls = getattr(m,class_name)

obj = cls()

obj.process_request()