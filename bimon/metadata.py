# -*- coding: utf-8 -*-


class Metadata:
    def __init__(self):
        self.__version__ = '0.1.0'
        self.__author__ = 'lokiheero'

    def get_version(self):
        return self.__version__

    def get_author(self):
        return self.__author__