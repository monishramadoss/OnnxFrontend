import numpy as np
from __future__ import absolute_import
from __future__ import division

class OneHot_9:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, indices: str, depth: str, values: str):
		input = (self.tensor[indices], self.tensor[depth], self.tensor[values])
		return self.tensor[output]
