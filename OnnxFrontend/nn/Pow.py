import numpy as np
from __future__ import absolute_import
from __future__ import division

class Pow_1:

	axis = m_int()
	broadcast = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int, broadcast: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_broadcast = broadcast

	def __call__(self, X: str, Y: str):
		input = (self.tensor[X], self.tensor[Y])
		return self.tensor[Z]


class Pow_7:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, X: str, Y: str):
		input = (self.tensor[X], self.tensor[Y])
		return self.tensor[Z]
