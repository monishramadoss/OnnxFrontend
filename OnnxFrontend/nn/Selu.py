import numpy as np
from __future__ import absolute_import
from __future__ import division

class Selu_1:

	alpha = m_float()
	consumed_inputs = m_list()
	gamma = m_float()
	def __init__(self, _name: str, _tensor: dict, alpha: float, consumed_inputs: list, gamma: float):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs
		self.m_gamma = gamma

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]


class Selu_6:

	alpha = m_float()
	gamma = m_float()
	def __init__(self, _name: str, _tensor: dict, alpha: float, gamma: float):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_gamma = gamma

	def __call__(self, X: str):
		input = (self.tensor[X])
		return self.tensor[Y]
