# _*_ coding:UTF-8 _*_
"""
抽象类：
	抽象方法：Add，update，delete，check
"""

from abc import *

class Services(metaclass=ABCMeta):
	@abstractclassmethod
	def add(self): pass
	@abstractclassmethod
	def update(self): pass
	@abstractclassmethod
	def delete(self): pass
	@abstractclassmethod
	def check(self): pass
