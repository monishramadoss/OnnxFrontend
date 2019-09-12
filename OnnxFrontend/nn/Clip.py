import numpy as np
from __future__ import absolute_import
from __future__ import division

class Clip_1:

	consumed_inputs = m_list()
	max = m_float()
	min = m_float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list, max: float, min: float):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_max = max
		self.m_min = min

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]


class Clip_6:

	max = m_float()
	min = m_float()
	def __init__(self, _name: str, _tensor: dict, max: float, min: float):
		self.name = _name
		self.tensor = _tensor
		self.m_max = max
		self.m_min = min

	def __call__(self, input: str):
		input = (self.tensor[input])
		return self.tensor[output]
