import numpy as np
from __future__ import absolute_import
from __future__ import division

class Reshape_1:

	consumed_inputs = m_list()
	shape = m_list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list, shape: list):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_shape = shape

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[reshaped]


class Reshape_5:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, data: str, shape: str):
		input = (self.tensor[data], self.tensor[shape])
		return self.tensor[reshaped]
