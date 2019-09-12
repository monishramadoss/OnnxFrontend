import numpy as np
from __future__ import absolute_import
from __future__ import division

class Gather_1:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, data: str, indices: str):
		input = (self.tensor[data], self.tensor[indices])
		return self.tensor[output]
