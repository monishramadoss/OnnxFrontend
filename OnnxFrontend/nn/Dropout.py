from __future__ import absolute_import
from __future__ import division
import numpy as np

class Dropout_1:

	m_consumed_inputs = list()
	m_is_test = int()
	m_ratio = float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list(), is_test=int(), ratio=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_is_test = is_test
		self.m_ratio = ratio

	def output(self, output, mask):
		self.m_output = output
		self.m_mask = mask


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output, self.m_mask])


class Dropout_6:

	m_is_test = int()
	m_ratio = float()
	def __init__(self, _name: str, _tensor: dict, is_test=int(), ratio=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_is_test = is_test
		self.m_ratio = ratio

	def output(self, output, mask):
		self.m_output = output
		self.m_mask = mask


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output, self.m_mask])


class Dropout_7:

	m_ratio = float()
	def __init__(self, _name: str, _tensor: dict, ratio=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_ratio = ratio

	def output(self, output, mask):
		self.m_output = output
		self.m_mask = mask


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output, self.m_mask])


class Dropout_10:

	m_ratio = float()
	def __init__(self, _name: str, _tensor: dict, ratio=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_ratio = ratio

	def output(self, output, mask):
		self.m_output = output
		self.m_mask = mask


	def __call__(self, data: str):
		self.m_data = data

		return (self.tensor[self.m_output, self.m_mask])
