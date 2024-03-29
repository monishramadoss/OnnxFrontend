from __future__ import absolute_import
from __future__ import division
import numpy as np

class Min_1:

	m_consumed_inputs = list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs

	def output(self, min=str()):
		self.m_min = min


	def __call__(self, data_0=str()):
		self.m_data_0 = data_0

		return (self.tensor[self.m_min])


class Min_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, min=str()):
		self.m_min = min


	def __call__(self, data_0=str()):
		self.m_data_0 = data_0

		return (self.tensor[self.m_min])


class Min_8:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, min=str()):
		self.m_min = min


	def __call__(self, data_0=str()):
		self.m_data_0 = data_0

		return (self.tensor[self.m_min])
