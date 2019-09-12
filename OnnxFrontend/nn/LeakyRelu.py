import numpy as np
from __future__ import absolute_import
from __future__ import division

class LeakyRelu_1:

	alpha = m_float()
	consumed_inputs = m_list()
	def __init__(self, _name: str, _tensor: dict, alpha: float, consumed_inputs: list):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class LeakyRelu_6:

	alpha = m_float()
	def __init__(self, _name: str, _tensor: dict, alpha: float):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
