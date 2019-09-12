import numpy as np
from __future__ import absolute_import
from __future__ import division

class Flatten_1:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]


class Flatten_9:

	axis = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
