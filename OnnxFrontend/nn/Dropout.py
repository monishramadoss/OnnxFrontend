import numpy as np
from __future__ import absolute_import
from __future__ import division

class Dropout_1:

	consumed_inputs = m_list()
	is_test = m_int()
	ratio = m_float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs: list, is_test: int, ratio: float):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_is_test = is_test
		self.m_ratio = ratio

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[output], self.tensor[mask]


class Dropout_6:

	is_test = m_int()
	ratio = m_float()
	def __init__(self, _name: str, _tensor: dict, is_test: int, ratio: float):
		self.name = _name
		self.tensor = _tensor
		self.m_is_test = is_test
		self.m_ratio = ratio

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[output], self.tensor[mask]


class Dropout_7:

	ratio = m_float()
	def __init__(self, _name: str, _tensor: dict, ratio: float):
		self.name = _name
		self.tensor = _tensor
		self.m_ratio = ratio

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[output], self.tensor[mask]


class Dropout_10:

	ratio = m_float()
	def __init__(self, _name: str, _tensor: dict, ratio: float):
		self.name = _name
		self.tensor = _tensor
		self.m_ratio = ratio

	def __call__(self, data: str):
		input = (self.tensor[data])
		return self.tensor[output], self.tensor[mask]
