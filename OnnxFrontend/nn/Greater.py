import numpy as np
from __future__ import absolute_import
from __future__ import division

class Greater_1:

	axis = m_int()
	broadcast = m_int()
	def __init__(self, _name: str, _tensor: dict, axis: int, broadcast: int):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis
		self.m_broadcast = broadcast

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[C]


class Greater_7:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[C]


class Greater_9:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, A: str, B: str):
		input = (self.tensor[A], self.tensor[B])
		return self.tensor[C]
