import numpy as np
from __future__ import absolute_import
from __future__ import division

class TopK_1:

	axis = m_int()
	k = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int, k: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_k = k

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Values], self.tensor[Indices]


class TopK_10:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, X: str, K: str):
		input = (self.tensor[X], self.tensor[K])
		return self.tensor[Values], self.tensor[Indices]
