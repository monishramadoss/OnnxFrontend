import numpy as np
from __future__ import absolute_import
from __future__ import division

class CategoryMapper_1:

	cats_int64s = m_list()
	cats_strings = m_list()
	default_int64 = m_int()
	default_string = m_str()
	def __init__(self, _name: str, _tensor: dict, cats_int64s: list, cats_strings: list, default_int64: int, default_string: str):
		self.name = _name
		self.tensor = _tensor
		self.m_cats_int64s = cats_int64s
		self.m_cats_strings = cats_strings
		self.m_default_int64 = default_int64
		self.m_default_string = default_string

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
