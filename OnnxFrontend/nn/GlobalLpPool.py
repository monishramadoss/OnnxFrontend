import numpy as np
from __future__ import absolute_import
from __future__ import division

class GlobalLpPool_1:

	p = m_float()
	def __init__(self, _name: str, _tensor: dict, p: float):
		self.name = _name
		self.tensor = _tensor
		self.m_p = p

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class GlobalLpPool_2:

	p = m_int()
	def __init__(self, _name: str, _tensor: dict, p: int):
		self.name = _name
		self.tensor = _tensor
		self.m_p = p

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
