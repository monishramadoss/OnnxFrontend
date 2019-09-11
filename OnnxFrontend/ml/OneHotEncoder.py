import numpy as np

class OneHotEncoder_1:

	cats_int64s = m_list()
	cats_strings = m_list()
	zeros = m_int()
	def __init__(self, _name: str, cats_int64s: list, cats_strings: list, zeros: int):
		self.name = _name
		self.m_cats_int64s = cats_int64s
		self.m_cats_strings = cats_strings
		self.m_zeros = zeros

	def __call__(self, X: str):
		 return Y
