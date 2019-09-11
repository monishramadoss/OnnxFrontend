import numpy as np

class ArgMax_1:

	axis = m_int()
	keepdims = m_int()
	def __init__(self, _name: str, axis: int, keepdims: int):
		self.name = _name
		self.m_axis = axis
		self.m_keepdims = keepdims

	def __call__(self, data: str):
		 return reduced
