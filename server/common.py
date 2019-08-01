import os

class file:
    def get_root_dic():
        return os.path.dirname(os.path.abspath(__file__))

    def get_cache_dic():
        return get_root_dic()+'\cache'
