import numpy as np
from __future__ import absolute_import
from __future__ import division

class Mean_1:

	consumed_inputs = m_list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, data_0: str):
		input = (self.tensor[data_0])
		return self.tensor[mean]


class Mean_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, data_0: str):
		input = (self.tensor[data_0])
		return self.tensor[mean]


class Mean_8:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def __call__(self, data_0: str):
		input = (self.tensor[data_0])
		return self.tensor[mean]
