from __future__ import absolute_import
from __future__ import division
import numpy as np

class Reshape_1:

	m_consumed_inputs = list()
	m_shape = list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list(), shape=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_shape = shape

	def output(self, reshaped):
		self.m_reshaped = reshaped


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_reshaped])


class Reshape_5:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, reshaped):
		self.m_reshaped = reshaped


	def __call__(self, data: str, shape: str):
		self.m_data = data
		self.m_shape = shape

		return (self.tensor[self.m_reshaped])
