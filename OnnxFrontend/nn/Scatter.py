import numpy as np
from __future__ import absolute_import
from __future__ import division

class Scatter_9:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, data: str, indices: str, updates: str):
		input = (self.tensor[data], self.tensor[indices], self.tensor[updates])
		return self.tensor[output]
