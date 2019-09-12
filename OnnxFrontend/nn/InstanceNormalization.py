import numpy as np
from __future__ import absolute_import
from __future__ import division

class InstanceNormalization_1:

	consumed_inputs = m_list()
	epsilon = m_float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list, epsilon: float):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_epsilon = epsilon

	def __call__(self, input: str, scale: str, B: str):
		input = (self.tensor[input], self.tensor[scale], self.tensor[B])
		return self.tensor[output]


class InstanceNormalization_6:

	epsilon = m_float()
	def __init__(self, _name: str, _tensor: dict, epsilon: float):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon

	def __call__(self, input: str, scale: str, B: str):
		input = (self.tensor[input], self.tensor[scale], self.tensor[B])
		return self.tensor[output]
