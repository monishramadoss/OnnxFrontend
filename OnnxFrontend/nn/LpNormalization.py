import numpy as np
from __future__ import absolute_import
from __future__ import division

class LpNormalization_1:

	axis = m_int()
	p = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int, p: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_p = p

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
