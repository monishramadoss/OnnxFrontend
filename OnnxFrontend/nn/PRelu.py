from __future__ import absolute_import
from __future__ import division
import numpy as np

class PRelu_1:

	m_consumed_inputs = list()
	def __init__(self, _name: str, _tensor: dict, consumed_inputs=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_consumed_inputs = consumed_inputs

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str(), slope=str()):
		self.m_X = X
		self.m_slope = slope

		return (self.tensor[self.m_Y])


class PRelu_6:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str(), slope=str()):
		self.m_X = X
		self.m_slope = slope

		return (self.tensor[self.m_Y])


class PRelu_7:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str(), slope=str()):
		self.m_X = X
		self.m_slope = slope

		return (self.tensor[self.m_Y])


class PRelu_9:

	def __init__(self, _name: str, _tensor: dict):
		self.name = _name
		self.tensor = _tensor

	def output(self, Y=str()):
		self.m_Y = Y


	def __call__(self, X=str(), slope=str()):
		self.m_X = X
		self.m_slope = slope

		return (self.tensor[self.m_Y])
