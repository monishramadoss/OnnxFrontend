from __future__ import absolute_import
from __future__ import division
import numpy as np

class CategoryMapper_1:

	m_cats_int64s = list()
	m_cats_strings = list()
	m_default_int64 = int()
	m_default_string = str()
	def __init__(self, _name: str, _tensor: dict, cats_int64s=list(), cats_strings=list(), default_int64=int(), default_string=str()):
		self.name = _name
		self.tensor = _tensor
		self.m_cats_int64s = cats_int64s
		self.m_cats_strings = cats_strings
		self.m_default_int64 = default_int64
		self.m_default_string = default_string

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str()):
		self.m_X = X

		return (self.tensor[self.m_Y])
