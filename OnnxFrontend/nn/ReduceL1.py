import numpy as np

class ReduceL1_1:

	axes = m_list()
	keepdims = m_int()
	def __init__(self, _name: str, axes: list, keepdims: int):
		self.name = _name
		self.m_axes = axes
		self.m_keepdims = keepdims

	def __call__(self, data: str):
		 return reduced
