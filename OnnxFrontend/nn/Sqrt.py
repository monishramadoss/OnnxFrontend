import numpy as np
from __future__ import absolute_import
from __future__ import division

class Sqrt_1:

	consumed_inputs = m_list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class Sqrt_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
