from __future__ import absolute_import
from __future__ import division
import numpy as np

class Selu_1:

	m_alpha = float()
	m_consumed_inputs = list()
	m_gamma = float()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), consumed_inputs=list(), gamma=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_consumed_inputs = consumed_inputs
		self.m_gamma = gamma

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])


class Selu_6:

	m_alpha = float()
	m_gamma = float()
	def __init__(self, _name: str, _tensor: dict, alpha=float(), gamma=float()):
		self.name = _name
		self.tensor = _tensor
		self.m_alpha = alpha
		self.m_gamma = gamma

	def output(self, Y):
		self.m_Y = Y


	def __call__(self, X: str):
		self.m_X = X

		return (self.tensor[self.m_Y])
