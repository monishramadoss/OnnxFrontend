from __future__ import absolute_import
from __future__ import division
import numpy as np

class Concat_1:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, concat_result):
		self.m_concat_result = concat_result


	def __call__(self, inputs: str):
		self.m_inputs = inputs

		return (self.tensor[self.m_concat_result])


class Concat_4:

	m_axis = int()
	def __init__(self, _name: str, _tensor: dict, axis=int()):
		self.name = _name
		self.tensor = _tensor
		self.m_axis = axis

	def output(self, concat_result):
		self.m_concat_result = concat_result


	def __call__(self, inputs: str):
		self.m_inputs = inputs

		return (self.tensor[self.m_concat_result])
