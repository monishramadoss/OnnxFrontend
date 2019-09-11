import numpy as np

class LpNormalization_1:

	axis = m_int()
	p = m_int()
	def __init__(self, _name: str, axis: int, p: int):
		self.name = _name
		self.m_axis = axis
		self.m_p = p

	def __call__(self, input: str):
		 return output
