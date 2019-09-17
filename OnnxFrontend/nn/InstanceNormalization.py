from __future__ import absolute_import
from __future__ import division
import numpy as np

class InstanceNormalization_1:

	m_consumed_inputs = list()
	m_epsilon = float()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list(), epsilon=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs
		self.m_epsilon = epsilon

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str(), scale=str(), B=str()):
		self.m_input = input
		self.m_scale = scale
		self.m_B = B

		return (self.tensor[self.m_output])


class InstanceNormalization_6:

	m_epsilon = float()
	def __init__(self, _name: str, _tensor: dict, epsilon=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_epsilon = epsilon

	def output(self, output=str()):
		self.m_output = output


	def __call__(self, input=str(), scale=str(), B=str()):
		self.m_input = input
		self.m_scale = scale
		self.m_B = B

		return (self.tensor[self.m_output])
