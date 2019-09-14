from __future__ import absolute_import
from __future__ import division
import numpy as np

class Elu_1:

	m_alpha = float()
	m_consumed_inputs = list()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), consumed_inputs=list()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])


class Elu_6:

	m_alpha = float()
	def __init__(self, _name: str, _tensor: dict, alpha=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
