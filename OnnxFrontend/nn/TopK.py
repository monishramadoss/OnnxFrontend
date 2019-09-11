import numpy as np

class TopK_1:

	axis = m_int()
	k = m_int()
	def __init__(self, _name: str, axis: int, k: int):
		self.name = _name
		self.m_axis = axis
		self.m_k = k

	def __call__(self, X: str):
		 return Values, Indices


class TopK_10:

	axis = m_int()
	def __init__(self, _name: str, axis: int):
		self.name = _name
		self.m_axis = axis

	def __call__(self, X: str, K: str):
		 return Values, Indices
