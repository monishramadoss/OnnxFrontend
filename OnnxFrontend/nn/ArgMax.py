import numpy as np
from __future__ import absolute_import
from __future__ import division

class ArgMax_1:

	axis = m_int()
	keepdims = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int, keepdims: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_keepdims = keepdims

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[reduced]
