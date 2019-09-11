import numpy as np

class ZipMap_1:

	classlabels_int64s = m_list()
	classlabels_strings = m_list()
	def __init__(self, _name: str, classlabels_int64s: list, classlabels_strings: list):
		self.name = _name
		self.m_classlabels_int64s = classlabels_int64s
		self.m_classlabels_strings = classlabels_strings

	def __call__(self, X: str):
		 return Z
