import numpy as np
from __future__ import absolute_import
from __future__ import division

class Cast_1:

	to = m_str()
	def __init__(self, _name: str, _tensor: dict, to: str):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]


class Cast_6:

	to = m_int()
	def __init__(self, _name: str, _tensor: dict, to: int):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]


class Cast_9:

	to = m_int()
	def __init__(self, _name: str, _tensor: dict, to: int):
		self.name = _name
		self.tensor = _tensor
		self.m_to = to

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
