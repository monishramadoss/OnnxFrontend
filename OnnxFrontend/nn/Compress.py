import numpy as np
from __future__ import absolute_import
from __future__ import division

class Compress_9:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, input: str, condition: str):
		input = (self.tensor[input], self.tensor[condition])
		return self.tensor[output]
